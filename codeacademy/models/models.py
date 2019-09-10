# -*- coding: utf-8 -*-

from datetime import timedelta
from odoo import models, fields, api, exceptions

class codeacademy(models.Model):
    _name = 'codeacademy.codeacademy'

    name = fields.Char()

class Course(models.Model):
    _name = 'codeacademy.course'
    _description = "Code Academy Courses"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

    responsible_id = fields.Many2one('res.users',ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many('codeacademy.session','course_id', string="Sessions")

    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Course, self).copy(default)


    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]


class Session(models.Model):
    _name = 'codeacademy.session'
    _description = "CodeAcademy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)

    duration = fields.Float(digits=(6, 2), help="Duration in days")

    seats = fields.Integer(string="Number of seats")
    active = fields.Boolean(default=True)

    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('codeacademy.course', ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')
    attendees_count = fields.Integer(string="Attendees count", compute='_get_attendees_count', store=True)

    # end_date = fields.Date(string="End Date", store=True, compute='_get_end_date', inverse='_set_end_date')
    end_date = fields.Date(default=fields.Date.today)
    # end_date2 = fields.Date(string="End Date 2", store=True, compute='_get_end_date', inverse='_set_end_date')
    #
    # hours = fields.Float(string="Duration in hours", compute='_get_hours', inverse='_set_hours')

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Seats alanı için geçersiz değer",
                    'message': "Katılımcı sayısı alanı negatif değer alamaz.",
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Katılımcı sayısı fazla",
                    'message': "Uygun yer sayısını arttırın veya katılımcı sayısını azaltın",
                },
            }

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_ids:
                raise exceptions.ValidationError("Kişi aynı anda hem eğitmen hem katılımcı olamaz")

    @api.depends('duration')
    def _get_hours(self):
        for r in self:
            r.hours = r.duration * 24

    def _set_hours(self):
        for r in self:
            r.duration = r.hours / 24

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date2 = r.start_date
                continue

                duration = timedelta(days=r.duration, seconds=-1)
                r.end_date2 = r.start_date + duration

    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date2):
                continue

            r.duration = (r.end_date2 - r.start_date).days + 1

    @api.depends('attendee_ids')
    def _get_attendees_count(self):
        for r in self:
            r.attendees_count = len(r.attendee_ids)







