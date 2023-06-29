from datetime import datetime, timezone

from astrolight.times import Location, SunriseTime, SunsetTime

TIMEZONE = timezone.utc


def test_sunrise_time() -> None:
    time = datetime(2023, 6, 23, tzinfo=TIMEZONE)
    location = Location(latitude=57.708870, longitude=11.974560)

    sunrise = SunriseTime().anchor(time, location)
    assert sunrise == time.replace(hour=2, minute=12)


def test_sunset_time() -> None:
    time = datetime(2023, 6, 23, tzinfo=TIMEZONE)
    location = Location(latitude=57.708870, longitude=11.974560)

    sunrise = SunsetTime().anchor(time, location)
    assert sunrise == time.replace(hour=20, minute=17)
