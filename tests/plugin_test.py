from fake import fake_group_message_event_v11
from nonebug import App
import pytest
from datetime import datetime
from unittest.mock import patch, Mock


@pytest.mark.asyncio
async def test_fupan_checkin(app: App):
    """Test the fupan checkin functionality"""
    import nonebot
    from nonebot.adapters.onebot.v11 import Adapter as OnebotV11Adapter
    from nonebot.adapters.onebot.v11 import Bot

    # Mock the datetime to ensure consistent timestamps
    fixed_datetime = datetime(2025, 9, 25, 15, 47, 12)

    event = fake_group_message_event_v11(message="复盘")
    try:
        from nonebot_plugin_fupan import fupan_checkin  # type:ignore
    except ImportError:
        pytest.skip("nonebot_plugin_fupan.fupan_checkin not found")

    with patch('nonebot_plugin_fupan.get_current_datetime', return_value=fixed_datetime):
        async with app.test_matcher(fupan_checkin) as ctx:
            adapter = nonebot.get_adapter(OnebotV11Adapter)
            bot = ctx.create_bot(base=Bot, adapter=adapter)

            # Mock the API calls that uninfo will make
            ctx.should_call_api("get_group_info", {"group_id": event.group_id}, {"group_id": event.group_id, "group_name": "test_group"})
            ctx.should_call_api("get_group_member_info", {"group_id": event.group_id, "user_id": event.user_id, "no_cache": True}, {"group_id": event.group_id, "user_id": event.user_id, "nickname": "test", "card": ""})

            ctx.receive_event(bot, event)
            # 根据时间窗口，可能成功也可能失败，这里只测试是否能正常处理
            # We expect a success response since we're within the time窗口
            expected_message = "✅ 复盘打卡成功！\n"
            expected_message += "━━━━━━━━━━━━━━━━\n"
            expected_message += "  打卡时间：2025-09-25 15:47:12\n"
            expected_message += "  累计打卡：1次\n"
            expected_message += "  连续打卡：1连击\n"
            expected_message += "━━━━━━━━━━━━━━━━\n"
            expected_message += "  交易日（2025年09月25日）已复盘\n"
            expected_message += "  下一个交易日：2025年09月26日"
            ctx.should_call_send(event, expected_message)
            ctx.should_finished()


@pytest.mark.asyncio
async def test_daka_alias(app: App):
    """Test the daka alias"""
    import nonebot
    from nonebot.adapters.onebot.v11 import Adapter as OnebotV11Adapter
    from nonebot.adapters.onebot.v11 import Bot

    # Mock the datetime to ensure consistent timestamps
    fixed_datetime = datetime(2025, 9, 25, 15, 47, 12)

    event = fake_group_message_event_v11(message="打卡")
    try:
        from nonebot_plugin_fupan import fupan_checkin  # type:ignore
    except ImportError:
        pytest.skip("nonebot_plugin_fupan.fupan_checkin not found")

    with patch('nonebot_plugin_fupan.get_current_datetime', return_value=fixed_datetime):
        async with app.test_matcher(fupan_checkin) as ctx:
            adapter = nonebot.get_adapter(OnebotV11Adapter)
            bot = ctx.create_bot(base=Bot, adapter=adapter)

            ctx.receive_event(bot, event)
            # 测试是否能正常处理
            # We expect a success response since we're within the time window
            expected_message = "✅ 复盘打卡成功！\n"
            expected_message += "━━━━━━━━━━━━━━━━\n"
            expected_message += "  打卡时间：2025-09-25 15:47:12\n"
            expected_message += "  累计打卡：1次\n"
            expected_message += "  连续打卡：1连击\n"
            expected_message += "━━━━━━━━━━━━━━━━\n"
            expected_message += "  交易日（2025年09月25日）已复盘\n"
            expected_message += "  下一个交易日：2025年09月26日"
            ctx.should_call_send(event, expected_message)
            ctx.should_finished()


@pytest.mark.asyncio
async def test_qiandao_alias(app: App):
    """Test the qiandao alias"""
    import nonebot
    from nonebot.adapters.onebot.v11 import Adapter as OnebotV11Adapter
    from nonebot.adapters.onebot.v11 import Bot

    # Mock the datetime to ensure consistent timestamps
    fixed_datetime = datetime(2025, 9, 25, 15, 47, 12)

    event = fake_group_message_event_v11(message="签到")
    try:
        from nonebot_plugin_fupan import fupan_checkin  # type:ignore
    except ImportError:
        pytest.skip("nonebot_plugin_fupan.fupan_checkin not found")

    with patch('nonebot_plugin_fupan.get_current_datetime', return_value=fixed_datetime):
        async with app.test_matcher(fupan_checkin) as ctx:
            adapter = nonebot.get_adapter(OnebotV11Adapter)
            bot = ctx.create_bot(base=Bot, adapter=adapter)

            ctx.receive_event(bot, event)
            # 测试是否能正常处理
            # We expect a success response since we're within the time窗口
            expected_message = "✅ 复盘打卡成功！\n"
            expected_message += "━━━━━━━━━━━━━━━━\n"
            expected_message += "  打卡时间：2025-09-25 15:47:12\n"
            expected_message += "  累计打卡：1次\n"
            expected_message += "  连续打卡：1连击\n"
            expected_message += "━━━━━━━━━━━━━━━━\n"
            expected_message += "  交易日（2025年09月25日）已复盘\n"
            expected_message += "  下一个交易日：2025年09月26日"
            ctx.should_call_send(event, expected_message)
            ctx.should_finished()


@pytest.mark.asyncio
async def test_fupan_stats(app: App):
    """Test the fupan stats command"""
    import nonebot
    from nonebot.adapters.onebot.v11 import Adapter as OnebotV11Adapter
    from nonebot.adapters.onebot.v11 import Bot

    event = fake_group_message_event_v11(message="复盘统计")
    try:
        from nonebot_plugin_fupan import fupan_stats  # type:ignore
    except ImportError:
        pytest.skip("nonebot_plugin_fupan.fupan_stats not found")

    async with app.test_matcher(fupan_stats) as ctx:
        adapter = nonebot.get_adapter(OnebotV11Adapter)
        bot = ctx.create_bot(base=Bot, adapter=adapter)

        ctx.receive_event(bot, event)
        # 测试是否能正常处理统计命令
        # For stats command, we expect a different message
        expected_message = "📈 您的群组复盘打卡统计\n"
        expected_message += "━━━━━━━━━━━━━━━━\n"
        expected_message += "  总打卡次数：0次\n"
        expected_message += "  连续打卡次数：0连击\n"
        expected_message += "━━━━━━━━━━━━━━━━\n\n"
        expected_message += "📚 暂无打卡记录\n"
        ctx.should_call_send(event, expected_message)
        ctx.should_finished()


@pytest.mark.asyncio
async def test_fupan_rank(app: App):
    """Test the fupan rank command"""
    import nonebot
    from nonebot.adapters.onebot.v11 import Adapter as OnebotV11Adapter
    from nonebot.adapters.onebot.v11 import Bot

    event = fake_group_message_event_v11(message="复盘排行")
    try:
        from nonebot_plugin_fupan import fupan_rank  # type:ignore
    except ImportError:
        pytest.skip("nonebot_plugin_fupan.fupan_rank not found")

    async with app.test_matcher(fupan_rank) as ctx:
        adapter = nonebot.get_adapter(OnebotV11Adapter)
        bot = ctx.create_bot(base=Bot, adapter=adapter)

        ctx.receive_event(bot, event)
        # 测试是否能正常处理排行命令
        # For rank command, we expect a different message
        ctx.should_call_send(event, "🏆 群组复盘连续打卡排行\n━━━━━━━━━━━━━━━━\n  暂无数据\n━━━━━━━━━━━━━━━━")
        ctx.should_finished()


@pytest.mark.asyncio
async def test_fupan_revoke(app: App):
    """Test the fupan revoke command"""
    import nonebot
    from nonebot.adapters.onebot.v11 import Adapter as OnebotV11Adapter
    from nonebot.adapters.onebot.v11 import Bot

    event = fake_group_message_event_v11(message="复盘撤销")
    try:
        from nonebot_plugin_fupan import fupan_revoke  # type:ignore
    except ImportError:
        pytest.skip("nonebot_plugin_fupan.fupan_revoke not found")

    async with app.test_matcher(fupan_revoke) as ctx:
        adapter = nonebot.get_adapter(OnebotV11Adapter)
        bot = ctx.create_bot(base=Bot, adapter=adapter)

        ctx.receive_event(bot, event)
        # 测试是否能正常处理撤销命令
        # For revoke command, we expect a different message
        ctx.should_call_send(event, "您还没有任何打卡记录，无需撤销")
        ctx.should_finished()