from . import db


class Kids(db.Model):
    __tablename__ = 'kids'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    phone = db.Column(db.String(32), unique=True, index=True)
    last_name = db.Column(db.String(64))
    first_name = db.Column(db.String(64))
    preferred_name = db.Column(db.String(64))
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'))
    graduation_year = db.Column(db.Integer)
    is_active = db.Column(db.Boolean, default=True)


class Volunteers(db.Model):
    __tablename__ = 'volunteers'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    phone = db.Column(db.String(32), unique=True, index=True)
    last_name = db.Column(db.String(64))
    first_name = db.Column(db.String(64))
    preferred_name = db.Column(db.String(64))


class VolunteerRoles(db.Model):
    __tablename__ = 'volunteerroles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    @staticmethod
    def insert_roles():
        roles = ['Mentor', 'Instructor', 'Administrator']
        for r in roles:
            role = VolunteerRoles.query.filter_by(name=r).first()
            if role is None:
                role = VolunteerRoles(name=r)
            db.session.add(role)
        db.session.commit()


class Schools(db.Model):
    __tablename__ = 'schools'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

#     [
#     'George Washington',
#     'Mission',
#     'Thurgood Marshall',
#     'Galileo',
#     'Leadership',
#     'Lincoln',
#     'Lowell',
#     'Immaculate Conception Academy',
#     'KIPP',
#     'S.F. International High School',
#     'San Francisco Flex Academy',
# ]

