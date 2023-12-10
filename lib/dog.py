from models import Dog

def create_table(base, engine):
    # check test
   base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog) 
    session.commit()

def get_all(session):
    dogs = session.query(Dog)
    return [dog for dog in dogs]

def find_by_name(session, name):
    match = session.query(Dog).filter(Dog.name == name).first()
    return match

def find_by_id(session, id):
    match = session.query(Dog).filter(Dog.id == id).first()
    return match

def find_by_name_and_breed(session, name, breed):
    match = session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()
    return match

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()