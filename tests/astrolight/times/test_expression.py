import pytest
from pydantic import BaseModel
from typing import Literal

from astrolight.times import DynamicTimeExpression
from astrolight.times.dynamic_time import DynamicTime, OffsetTime


class DynamicTimeExpressionModel(BaseModel):
    expression: DynamicTimeExpression


def test_pydantic_parse_produces_right_class_type() -> None:
    model = DynamicTimeExpressionModel.parse_obj({"expression": "10:00"})

    assert isinstance(model.expression, DynamicTimeExpression)


@pytest.mark.parametrize(
    "expression, expr",
    [
        ("10:00", [("+", OffsetTime("10:00"))]),
        ("10:00 + 2:00", [("+", OffsetTime("10:00")), ("+", OffsetTime("2:00"))]),
    ],
)
def test_dynamic_time_expression_from_string(
    expression: str,
    expr: list[tuple[Literal["+", "-"], DynamicTime]],
) -> None:
    assert DynamicTimeExpression.from_string(expression) == DynamicTimeExpression(expr=expr)
