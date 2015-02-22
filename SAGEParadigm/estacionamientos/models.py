# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import RegexValidator

# Validators

RIF_Validator = RegexValidator(
				regex = '^[JVD]-?\d{8}-?\d$', 
				message = 'Introduzca un RIF con un formato válido.'
				)

CREDITCARD_Validator = RegexValidator(
						regex = '^\d{16}$',
						message = 'Introduzca un número de tarjeta de crédito con un formato válido.'
						)

PHONE_Validator = RegexValidator(
					regex = '^((0212)|(0412)|(0416)|(0414)|(0424)|(0426))-?\d{7}',
					message = 'Debe introducir un formato válido.'					
					)

# Choices

ESQUEMA_Choices = [("1", "Por hora"),
					("2", "Por hora y fracción"),
					("3", "Por minuto"),
					("4", "Diferenciado por hora")]


# Models

class Estacionamiento(models.Model):
	# propietario=models.ForeignKey(Propietario)
	Propietario = models.CharField(max_length = 50, help_text = "Nombre del Propietario", verbose_name="Nombre del Dueño")
	Nombre = models.CharField(max_length = 50, verbose_name="Nombre del Estacionamiento")
	Direccion = models.TextField(max_length = 120, verbose_name="Dirección")

	Telefono_1 = models.CharField(blank = True, null = True, max_length = 30, validators = [PHONE_Validator], verbose_name="Teléfono 1")
	Telefono_2 = models.CharField(blank = True, null = True, max_length = 30, validators = [PHONE_Validator], verbose_name="Teléfono 2")
	Telefono_3 = models.CharField(blank = True, null = True, max_length = 30, validators = [PHONE_Validator], verbose_name="Teléfono 3")

	Email_1 = models.EmailField(blank = True, null = True, verbose_name="Email 1")
	Email_2 = models.EmailField(blank = True, null = True, verbose_name="Email 2")

	Rif = models.CharField(max_length = 12, validators = [RIF_Validator], verbose_name="RIF")

	Esquema_tarifario = models.CharField(max_length = 4, choices = ESQUEMA_Choices, blank = True, null = True, verbose_name="Esquema Tarifario")
	Tarifa = models.DecimalField(max_digits=6, decimal_places=2, blank = True, null = True, verbose_name="Tarifa")
	HoraPicoInicio = models.TimeField(blank = True, null = True, verbose_name="Inicio de Hora Pico")
	HoraPicoFin = models.TimeField(blank = True, null = True, verbose_name="Fin de Hora Pico")
	TarifaPico = models.DecimalField(max_digits=6, decimal_places=2, blank = True, null = True, verbose_name="Tarifa de Hora Pico")
	
	Apertura = models.TimeField(blank = True, null = True, verbose_name="Horario de Apertura")
	Cierre = models.TimeField(blank = True, null = True, verbose_name="Horario de Cierre")
	Reservas_Inicio = models.TimeField(blank = True, null = True, verbose_name="Horario Inicio de Reserva")
	Reservas_Cierre = models.TimeField(blank = True, null = True, verbose_name="Horario Fin de Reserva")
	
	NroPuesto = models.IntegerField(blank = True, null = True, verbose_name="Número de Puestos")

	def __str__(self):
		return "Estacionamiento " + self.Nombre

# class ExtendedModel(models.Model):
# 	Estacionamiento = models.ForeignKey(Estacionamiento, primary_key = True)

# class EstacionamientoModelForm(EstacionamientoForm):
# 	class Meta:
# 		model = EstacionamientoModel
# 		fields = ['propietario', 'nombre', 'direccion', 'telefono_1', 'telefono_2', 'telefono_3', 'email_1',
# 				'email_2', 'rif', 'tarifa', 'horarioin', 'horariout', 'horario_resein', 'horario_reserout']

# class Propietario(models.Model):
	# nombre = models.CharField(max_length = 50, help_text = "Nombre Propio")

# class EstadoEstacionamiento(models.Model):
	#

# class PuestosModel(models.Model):
# 	estacionamiento = models.ForeignKey(ExtendedModel)


class ReservasModel(models.Model):
	Estacionamiento = models.ForeignKey(Estacionamiento)
	Puesto = models.IntegerField()
	InicioReserva = models.TimeField()
	FinalReserva = models.TimeField()
	Pagada = models.NullBooleanField(blank = True, null = True)

	def __str__(self):
		return "Reserva del puesto " + str(self.Puesto) + " en " + self.Estacionamiento.Nombre + " de " + str(self.InicioReserva) + " a " + str(self.FinalReserva)
