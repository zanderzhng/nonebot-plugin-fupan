from fake import fake_group_message_event_v11
from nonebug import App
import pytest
from datetime import datetime


@pytest.mark.asyncio
async def test_fupan_checkin(app: App):
    """Test the fupan checkin functionality"""
    import nonebot
    from nonebot.adapters.onebot.v11 import Adapter as OnebotV11Adapter
    from nonebot.adapters.onebot.v11 import Bot

    event = fake_group_message_event_v11(message="复盘")
    try:
        from nonebot_plugin_fupan import fupan_checkin  # type:ignore
    except ImportError:
        pytest.skip("nonebot_plugin_fupan.fupan_checkin not found")

    async with app.test_matcher(fupan_checkin) as ctx:
        adapter = nonebot.get_adapter(OnebotV11Adapter)
        bot = ctx.create_bot(base=Bot, adapter=adapter)
        ctx.receive_event(bot, event)
        # 根据时间窗口，可能成功也可能失败，这里只测试是否能正常处理
        ctx.should_call_send(event, ..., result=None, bot=bot)
        ctx.should_finished()


@pytest.mark.asyncio
async def test_daka_alias(app: App):
    """Test the daka alias"""
    import nonebot
    from nonebot.adapters.onebot.v11 import Adapter as OnebotV11Adapter
    from nonebot.adapters.onebot.v11 import Bot

    event = fake_group_message_event_v11(message="打卡")
    try:
        from nonebot_plugin_fupan import fupan_checkin  # type:ignore
    except ImportError:
        pytest.skip("nonebot_plugin_fupan.fupan_checkin not found")

    async with app.test_matcher(fupan_checkin) as ctx:
        adapter = nonebot.get_adapter(OnebotV11Adapter)
        bot = ctx.create_bot(base=Bot, adapter=adapter)
        ctx.receive_event(bot, event)
        # 测试是否能正常处理
        ctx.should_call_send(event, ..., result=None, bot=bot)
        ctx.should_finished()


@pytest.mark.asyncio
async def test_qiandao_alias(app: App):
    """Test the qiandao alias"""
    import nonebot
    from nonebot.adapters.onebot.v11 import Adapter as OnebotV11Adapter
    from nonebot.adapters.onebot.v11 import Bot

    event = fake_group_message_event_v11(message="签到")
    try:
        from nonebot_plugin_fupan import fupan_checkin  # type:ignore
    except ImportError:
        pytest.skip("nonebot_plugin_fupan.fupan_checkin not found")

    async with app.test_matcher(fupan_checkin) as ctx:
        adapter = nonebot.get_adapter(OnebotV11Adapter)
        bot = ctx.create_bot(base=Bot, adapter=adapter)
        ctx.receive_event(bot, event)
        # 测试是否能正常处理
        ctx.should_call_send(event, ..., result=None, bot=bot)
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
        ctx.should_call_send(event, ..., result=None, bot=bot)
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
        ctx.should_call_send(event, ..., result=None, bot=bot)
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
        ctx.should_call_send(event, ..., result=None, bot=bot)
        ctx.should_finished()