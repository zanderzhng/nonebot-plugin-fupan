import os
from pathlib import Path
from datetime import datetime

import nonebot
from nonebot.adapters.onebot.v11 import Adapter as OnebotV11Adapter
import pytest
from pytest_asyncio import is_async_test

os.environ["ENVIRONMENT"] = "test"


def pytest_collection_modifyitems(items: list[pytest.Item]):
    pytest_asyncio_tests = (item for item in items if is_async_test(item))
    session_scope_marker = pytest.mark.asyncio(loop_scope="session")
    for async_test in pytest_asyncio_tests:
        async_test.add_marker(session_scope_marker, append=False)


@pytest.fixture(scope="session", autouse=True)
async def after_nonebot_init(after_nonebot_init: None):
    """Initialize NoneBot"""
    # 加载适配器
    driver = nonebot.get_driver()
    driver.register_adapter(OnebotV11Adapter)

    # 加载插件
    nonebot.load_from_toml("pyproject.toml")

    # Yield control back to tests
    yield


@pytest.fixture(autouse=True)
def clear_test_data():
    """Clear test data before and after each test"""
    # Brute force approach: clear all checkin files in the entire project
    def clear_all_checkin_files():
        project_root = Path.cwd()
        deleted_files = []

        # Search the entire project for checkin files
        for file_path in project_root.rglob("checkin_*.json"):
            if file_path.is_file():
                try:
                    file_path.unlink()
                    deleted_files.append(str(file_path))
                except:
                    pass

        return deleted_files

    # Clear before test
    clear_all_checkin_files()
    yield
    # Clear after test
    clear_all_checkin_files()