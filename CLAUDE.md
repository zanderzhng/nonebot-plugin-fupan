# NoneBot Plugin Fupan Memory File

## Plugin Overview
- **Name**: nonebot-plugin-fupan
- **Description**: A NoneBot plugin for stock traders to record daily trade reviews and check-ins
- **Functionality**:
  - Daily check-in/review tracking
  - Trading day detection using exchange calendars
  - Time window control for check-ins
  - Personal statistics and group rankings
  - Data persistence using local storage

## Recent Improvements
- **Enhanced User Nickname Handling**: Improved user information retrieval using `nonebot_plugin_uninfo`
- **Separate Data Storage**: Different data files for group vs private message environments
- **Reset Functionality**: Added reset command for administrators
- **Help Command**: Added `/复盘帮助` command for user guidance
- **Improved Nickname Display**: Better nickname acquisition and display in rankings (platform dependent)
- **Enhanced Check-in Logging**: Detailed tracking of check-in information including timestamps, weekday distribution, and trading day context
- **Removed Limiter Dependency**: Simplified rate limiting by removing unnecessary dependency since users can only check in once per trading period
- **Strike Count Tracking**: Added consecutive check-in tracking based on continuous trading days
- **Ranking by Strike Count**: Modified ranking system to show users with the highest consecutive check-in streaks
- **Conclusion Attachment**: Users can now attach conclusions to their check-ins using `/复盘 我觉得明天高开低走` syntax

## Core Components

### Main Module (`src/nonebot_plugin_fupan/__init__.py`)
- **Commands**:
  - `复盘 [结论]` - Main command for daily review/check-in with optional conclusion
  - `打卡 [结论]` - Alias for 复盘
  - `签到 [结论]` - Alias for 复盘
  - `复盘统计` - View personal check-in statistics including strike count and conclusions
  - `复盘排行` - View group check-in rankings by strike count (consecutive check-ins)
  - `复盘撤销` - Revoke last check-in and update strike count
  - `复盘帮助` - Show help information
  - `复盘重置` - Reset data (admin only)

- **Key Functions**:
  - `get_checkin_data_file(user_id, group_id)` - Get user's data file path (group-specific)
  - `load_user_checkin_data(user_id, group_id)` - Load user's check-in data
  - `save_user_checkin_data(user_id, data, group_id)` - Save user's check-in data
  - `is_trading_day(date)` - Check if date is a trading day
  - `get_current_trading_status(user_id, group_id)` - Get current trading status and time window
  - `can_user_checkin(user_id, group_id)` - Check if user can check-in now
  - `reset_group_data(group_id)` - Reset all user data for a group
  - `reset_all_dm_data()` - Reset all private message user data
  - `calculate_strike_count(checkins)` - Calculate consecutive check-in streak based on trading days

- **Dependencies**:
  - `nonebot_plugin_uninfo` - Multi-platform user info
  - `nonebot_plugin_localstore` - Local data storage
  - `nonebot_plugin_apscheduler` - Scheduled tasks
  - `exchange_calendars` - Trading calendar system

### Configuration (`src/nonebot_plugin_fupan/config.py`)
- **Settings**:
  - `fupan_checkin_start_time` (default: "15:00") - Check-in window start
  - `fupan_checkin_end_time` (default: "09:00") - Check-in window end (next day)
  - `fupan_checkin_group_time_windows` - Per-group time window configuration
  - `fupan_checkin_user_time_windows` - Per-user time window configuration

### Data Structure
- **Storage Location**:
  - Group: `data/fupan/checkin_{user_id}_group_{group_id}.json`
  - Private Message: `data/fupan/checkin_{user_id}_dm.json`
- **Data Format**:
  ```json
  {
    "user_id": "user_id",
    "nickname": "user_nickname",
    "checkins": [
      {
        "date": "YYYY-MM-DD",
        "timestamp": 1234567890.123,
        "trading_day": "YYYY-MM-DD",  // Which trading day this check-in is for (always the previous trading day since check-ins happen after market close)
        "next_trading_day": "YYYY-MM-DD",  // Next trading day after this check-in's trading day (for efficient strike calculation)
        "context": "group/private",
        "conclusion": "optional conclusion text" // optional field for user's conclusion
      }
    ],
    "total_count": number,
    "strike_count": number
  }
  ```

## Key Features
1. **Trading Day Detection**: Uses Shanghai Stock Exchange calendar via `exchange-calendars`
2. **Time Window Control**: Configurable check-in time window (default 15:00 to next day 09:00)
3. **Duplicate Prevention**: Prevents multiple check-ins per day per user
4. **Statistics Tracking**: Personal check-in counts and group rankings
5. **Multi-Platform Support**: Works with various NoneBot adapters
6. **Environment Separation**: Separate data storage for group vs private message contexts
7. **Nickname Display**: Shows user nicknames instead of user IDs in rankings (platform dependent)
8. **Admin Reset**: Superuser can reset data for groups or private messages
9. **User Help**: Built-in help command for user guidance
10. **Detailed Logging**: Enhanced check-in logging with timestamps, weekday distribution, and trading day context
11. **Comprehensive Statistics**: Detailed personal statistics including weekday distribution and context-specific counts
12. **Strike Count Tracking**: Tracks consecutive trading day check-ins for streak building
13. **Ranking by Strike Count**: Group rankings based on consecutive check-in streaks rather than total counts

## Platform Limitations
- **Official QQ Bots**: User nickname information is not available due to platform restrictions. Nickname display feature works best with other bot adapters.

## Usage Instructions
1. Users can check-in with: `复盘`, `打卡`, or `签到` (optionally add conclusion text)
2. View personal stats: `复盘统计`
3. View group rankings: `复盘排行`
4. Revoke last check-in: `复盘撤销` or `撤销复盘`
5. Get help: `复盘帮助`
6. Admin reset: `复盘重置` (superuser only)
7. Configure time window in .env file
8. Example: `/复盘 我觉得明天高开低走`

## Installation Dependencies
- NoneBot2 >=2.4.3
- exchange-calendars >=4.11.1
- nonebot-plugin-localstore >=0.7.4
- nonebot-plugin-apscheduler >=0.5.0
- nonebot-plugin-uninfo >=0.9.0
- always use uv