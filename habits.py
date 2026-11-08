"""habits.py (Role B): add, remove, list and mark habits."""

import datetime

def parse_date(text):
  """Return a datetime.date for 'YYYY-MM-DD', or None if invalid."""
  if not isinstance(text, str) or len(text) != 10:
    return None
  try:
    return datetime.datetime.strptime(text, "%Y-%m-%d").date()
  except ValueError:
    return None


def add_habit(data, name):
  """Add a habit and return its new id as text.
  The name is stripped of spaces. If the name is empty (or not text), nothing is added and "" is returned. The new id is the highest numeric id l ("1" in empty data). The creation date is today."""
  if not isinstance (name, str):
    return ""
  name = name.strip()
  if name == "":
    return ""
  highest = 0
  for existing_id in data["habits"]:
    if existing_id.isdigit():
      highest = max(highest, int(existing_id))
  new_id = str(highest + 1)
  data["habits"][new_id] = {
    "name": name,
    "created": datetime.date.today().isoformat(),
  }
  return new_id


def remove_habit(data, habit_id):
  """Remove a habit and its log. Return False if the id doees nor exist."""
  if habit_id not in data["habits"]:
    return False
  del data["habits"][habit_id]
  data["log"].pop(habit_id, None)
  return True


def list_habits(data):
  """Return a list of (id, name) pairs in the stored order."""
  return [(habit_id, info["name"]) 
          for habit_id, info in data["habits"].items()]


def mark_done(data, habit_id, date):
  """Add a date (YYYY-MM-DD) to a habit's log.
  
  Return False if the id is unknown, the date is invalid, the date is in the future, or the date is already logged. Otherwise return True."""
  if habit_id not in data["habits"]:
    return False
  parsed = parse_date(date)
  if parsed is None:
    return False
  if parsed > datetime.date.today():
    return False
  dates = data["log"].setdefault(habit_id, [])
  if date in dates:
    return False
  dates.append(date)
  return True
 