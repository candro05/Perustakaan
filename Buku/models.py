from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Ketegori_Buku (models.Model):
    id_ketegori = models.CharField(max_length=100)
    nama_kategori =models.TextField(blank=True)

    def __str__(self):
        return self.nama_kategori

class Jenis_Buku (models.Model):
    id_jenis = models.CharField(max_length=100)
    jenis_buku = models.TextField(blank=True)

    def __str__(self):
        return self.jenis_buku

class Buku (models.Model):
    id_buku = models.CharField(max_length=100)
    nama_buku = models.CharField(max_length=100)
    penerbit = models.CharField(max_length=100)
    jumlah_buku = models.CharField(max_length=100)
    kategori_buku = models.ForeignKey(Ketegori_Buku, on_delete=models.CASCADE)
    jenis_buku = models.ForeignKey(Jenis_Buku, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_buku