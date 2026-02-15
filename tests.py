from app.agents import victim_respond, director_update, moderator_select

def test_victim():
    r = victim_respond("Hello", "Respond slowly", None)
    assert isinstance(r, str)

def test_director():
    obj = director_update("Computer problem", "Tech Support", "Respond slowly")
    assert isinstance(obj, str)

def test_moderator():
    winner = moderator_select(["Event1", "Event2"])
    assert winner in ["Event1", "Event2"]
