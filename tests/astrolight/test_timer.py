import pytest
from datetime import datetime

from astrolight.timer import Timer
from astrolight.times import DynamicTimeExpression, Location, OffsetTime

LOCATION = Location(latitude=0, longitude=0)


@pytest.mark.parametrize(
    "timestamp, active",
    [
        ("05:59", False),
        ("06:00", True),
        ("06:01", True),
        ("06:02", True),
        ("07:00", True),
        ("07:59", True),
        ("08:00", False),
    ],
)
def test_timer_is_active(timestamp: str, active: bool) -> None:
    timer = Timer(
        after=DynamicTimeExpression(expr=[("+", OffsetTime("06:00"))]),
        until=DynamicTimeExpression(expr=[("+", OffsetTime("08:00"))]),
    )

    time = datetime.fromisoformat(f"2023-06-23 {timestamp}")
    assert timer.is_active(time, LOCATION) is active
