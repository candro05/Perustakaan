from Buku.models import Ketegori_Buku, Jenis_Buku, Buku
from rest_framework import serializers

class BukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buku
        fields = ['id_buku', 'nama_buku', 'penerbit', 'jumlah_buku', 'kategori_buku', 'jenis_buku']
