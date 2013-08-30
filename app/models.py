from app import db

class Object(db.Model):
    obj_seq = db.Column(db.Integer, primary_key=True)
    obj_name = db.Column(db.String(120), unique=True)
    obj_phone = db.Column(db.String(120))
    obj_schema = db.Column(db.String(120))
    obj_path = db.Column(db.String(120))
    obj_photo_url = db.Column(db.String(120))
    obj_adress = db.Column(db.String(120))
    obj_category = db.Column(db.String(120))
    obj_priority = db.Column(db.Integer)
    obj_coord = db.Column(db.Integer)
    dvrs = db.relationship('Dvr', backref='object', lazy='dynamic')
    zones = db.relationship('Zone', backref='object', lazy='dynamic')
    regions = db.relationship('Region', backref='object', lazy='dynamic')

    def __init__(self, obj_name, obj_phone, obj_schema, obj_path, obj_photo_url, obj_adress, obj_category, obj_priority, obj_coord):

        self.obj_name = obj_name
        self.obj_phone = obj_phone
        self.obj_schema = obj_schema
        self.obj_path = obj_path
        self.obj_photo_url = obj_photo_url
        self.obj_adress = obj_adress
        self.obj_category = obj_category
        self.obj_priority = obj_priority
        self.obj_coord = obj_coord

    def __repr__(self):
        return "<Object %r>" % self.obj_name

object_person = db.Table('object_person',
        db.Column('obj_seq', db.Integer, db.ForeignKey('object.obj_seq')),
        db.Column('person_seq', db.Integer, db.ForeignKey('person.person_seq'))
    )

class Person (db.Model):
    person_seq = db.Column(db.Integer, primary_key=True)
    person_name = db.Column(db.String(120))
    person_lastname = db.Column(db.String(120))
    person_adress = db.Column(db.String(120))
    person_phone = db.Column(db.String(120))
    person_email = db.Column(db.String(120))
    person_photo = db.Column(db.String(120))
    person_is_customer = db.Column(db.Boolean)
    objects = db.relationship('Object', secondary=object_person, backref=db.backref('objects', lazy='dynamic'))

    def __init__(self, person_name, person_lastname, person_adress, person_phone, person_email, person_photo, person_is_customer, objects):
        if isinstance(objects, Object):
            self.album = objects
        else:
            raise TypeError('Invalid format !!!')
        self.person_name = person_name
        self.person_lastname = person_lastname
        self.person_adress = person_adress
        self.person_phone = person_phone
        self.person_email = person_email
        self.person_photo = person_photo
        self.person_is_customer = person_is_customer

    def __repr__(self):
        return "<Person %r>" % self.person_name, self.person_lastname

class Dvr(db.Model):
    dvr_seq = db.Column(db.Integer, primary_key=True)
    dvr_name = db.Column(db.String(120))
    dvr_ip = db.Column(db.String(120))
    obj_seq = db.Column(db.Integer, db.ForeignKey('object.obj_seq'))
    dvrs = db.relationship('Alert', backref='dvr', lazy='dynamic')
    #object = db.relationship('Object', backref=db.backref('dvrs', lazy='dynamic'))


    def __init__(self, dvr_name, dvr_ip, alert):
        if isinstance(alert, Alert):
            self.alert = alert
        else:
            raise TypeError('Invalid format !!!')
        self.dvr_name = dvr_name
        self.dvr_ip = dvr_ip

    def __repr__(self):
        return "<Dvr %r>" % self.dvr_ip

class Alert (db.Model):
    alert_seq = db.Column(db.Integer, primary_key=True)
    alert_date = db.Column(db.Date)
    alert_time = db.Column(db.Time)
    alert_photo_url = db.Column(db.String(120))
    alert_state = db.Column(db.Integer)
    dvr_seq = db.Column(db.Integer, db.ForeignKey('dvr.dvr_seq'))
    #dvr = db.relationship('Dvr', backref=db.backref('Dvr', lazy='dynamic'))

    def __init__(self, alert_date, alert_time, alert_photo_url, alert_state):

        self.alert_date = alert_date
        self.alert_time = alert_time
        self.alert_photo_url = alert_photo_url
        self.alert_state = alert_state

    def __repr__(self):
        return "<Alert %r>" % self.alert_date

class Zone(db.Model):
    zone_seq = db.Column(db.Integer, primary_key=True)
    zone_name = db.Column(db.String(120))
    obj_seq = db.Column(db.Integer, db.ForeignKey('object.obj_seq'))
    #object = db.relationship('Object', backref=db.backref('Object', lazy='dynamic'))

    def __init__(self, zone_name):

        self.zone_name = zone_name

    def __repr__(self):
        return "<Zone %r>" % self.zone_name

class Region(db.Model):
    region_seq = db.Column(db.Integer, primary_key=True)
    region_name = db.Column(db.String(120))
    obj_seq = db.Column(db.Integer, db.ForeignKey('object.obj_seq'))
    #object = db.relationship('Object', backref=db.backref('Object', lazy='dynamic'))

    def __init__(self, region_name):

        self.region_name = region_name

    def __repr__(self):
        return "<Region %r>" % self.region_name