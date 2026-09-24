import polars as pl

OPERATORS = {
    "==": lambda c, v: pl.col(c) == v,
    "!=": lambda c, v:pl.col(c) != v,
    ">": lambda c, v:pl.col(c) > v,
    ">=": lambda c, v:pl.col(c) >=v,
    "<": lambda c, v:pl.col(c) < v,
    "<=": lambda c, v:pl.col(c) <= v,
    "contains": lambda c, v:pl.col(c).str.contains(v),
    "in": lambda c, v:pl.col(c).is_in(v),

}