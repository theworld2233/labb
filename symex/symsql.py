## This module wraps SQLalchemy's methods to be friendly to
## symbolic / concolic execution.

import sqlalchemy.orm
from . import fuzzy

oldget = sqlalchemy.orm.query.Query.get
def newget(query, primary_key):
  ## Exercise 8: your code here.
  ##
  ## Find the object with the primary key "primary_key" in SQLalchemy
  ## query object "query", and do so in a symbolic-friendly way.
  ##
  ## Hint: given a SQLalchemy row object r, you can find the name of
  ## its primary key using r.__table__.primary_key.columns.keys()[0]
  rows = query.all()

  for r in query.all():
    primary_key_in_row = getattr(r, r.__table__.primary_key.columns.keys()[0])
    if primary_key_in_row == primary_key:
      return r

  return None

sqlalchemy.orm.query.Query.get = newget
