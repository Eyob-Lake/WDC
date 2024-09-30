from odoo import api, fields, models
from odoo.exceptions import ValidationError


class WudasiePatient(models.Model):
	_name = "wudasie.patient"
	_inherit = ['mail.thread']
	_description = "Patient Master"
	
	# Basic fields for patient information
	name = fields.Char(string="Name", required=True, tracking=True)
	age = fields.Integer(string="Age")  # Age field
	gender = fields.Selection(
		[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
		string="Gender",
		required=True,
		help="Select the gender of the patient"
	)
	date_of_visit = fields.Date(string="Date of Visit")  # Date of visit field
	phone_number = fields.Char(string="Phone Number")  # Phone number field
	prescription = fields.Binary(string="Prescription", attachment=True)  # PDF file upload field
	prescription_filename = fields.Char(string="Prescription Filename")  # Filename field
	
	# Fields for treated doctor and referred institution
	treated_doctor_id = fields.Many2one(
		'res.partner',
		string="Treated Doctor",
		domain="[('is_doctor', '=', True)]",  # Ensure only doctors are selectable
		required=True  # Ensure this field is mandatory
	)
	
	referred_institution_id = fields.Many2one(
		'res.partner',
		string="Referred Institution",
		domain="[('is_institution', '=', True)]"  # Ensure only institutions are selectable
	)
	
	@api.model
	def create(self, vals):
		"""Override the create method to validate treated doctor and institution."""
		self._validate_doctor_and_institution(vals)
		return super(WudasiePatient, self).create(vals)
	
	def write(self, vals):
		"""Override the write method to validate treated doctor and institution."""
		self._validate_doctor_and_institution(vals)
		return super(WudasiePatient, self).write(vals)
	
	def _validate_doctor_and_institution(self, vals):
		"""Check if treated doctor and referred institution fields are valid."""
		if 'treated_doctor_id' in vals and vals['treated_doctor_id']:
			doctor = self.env['res.partner'].browse(vals['treated_doctor_id'])
			if not doctor.exists() or not doctor.is_doctor:
				raise ValidationError("The selected treated doctor is not a valid doctor.")
		
		if 'referred_institution_id' in vals and vals['referred_institution_id']:
			institution = self.env['res.partner'].browse(vals['referred_institution_id'])
			if not institution.exists() or not institution.is_institution:
				raise ValidationError("The selected referred institution is not a valid institution.")
