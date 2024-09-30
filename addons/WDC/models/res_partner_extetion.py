from odoo import fields, models, api
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
	_inherit = 'res.partner'
	
	# Adding is_doctor and is_institution fields
	is_doctor = fields.Boolean(string="Is a Doctor", help="Check if this partner is a doctor.")
	is_institution = fields.Boolean(string="Is an Institution", help="Check if this partner is a medical institution.")
	
	def write(self, vals):
		"""Override write method to validate before updating."""
		for record in self:
			# Check if the partner is being set as a doctor
			if 'is_doctor' in vals and vals['is_doctor']:
				if not record.name:
					raise ValidationError("Cannot set 'Is a Doctor' to True if the partner does not have a name.")
				if not record.is_doctor:  # Ensure the partner is a valid doctor
					raise ValidationError("Cannot set 'Is a Doctor' to True if the partner is not a valid doctor.")
		return super(ResPartner, self).write(vals)
	
	@api.model
	def create(self, vals):
		"""Override create method to validate before creating a record."""
		if vals.get('is_doctor') and not vals.get('name'):
			raise ValidationError("A doctor must have a name.")
		return super(ResPartner, self).create(vals)
