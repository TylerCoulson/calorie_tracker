from datetime import date
import pytest
from app.api.calcs import calorie_calcs



def test_bmi(daily_output):
    assert daily_output.bmi() == 46.25

# @pytest.mark.parametrize(
#     "logs, date, start_date, expected",
#     [(70, date(2023,2,18), date(2023,2,17))]
# )
# def test_total_calories_eaten(logs, date, start_date, expected):
#     assert calorie_calcs.total_calories_eaten(logs, date, start_date) == expected


# @pytest.mark.parametrize(
#     "total_calories_eaten, start_weight, lbs_per_day, days, start_age, current_age, height, sex,   activity_level, expected",
#     [
#     (166511,               322.4,        2/7,         73,   29,        30,          70,     'male', 1.2,            310.2), 
#     (129102.1,             322.4,        2/7,         58,   30,        30,          70,     "male", 1.2,            311.7)
#     ]
# )
# def test_estimated_weight(total_calories_eaten, start_weight, lbs_per_day, days, start_age, current_age, height, sex, activity_level, expected):
#     result = calorie_calcs.estimated_weight(
#         total_calories_eaten, start_weight, lbs_per_day, days, start_age, current_age, height, sex, activity_level
#     )

    
#     assert result == expected


# @pytest.mark.parametrize(
#     "est_weight, goal_weight, rmr, weekly_lbs_lose, sex",
#     [(310.2,     150.0,         46.25)]
# )
# def test_calorie_goal(est_weight, goal_weight, rmr, weekly_lbs_lose, sex)