from rest_framework import serializers
from .models import Peep, Chirp

class ChirpSerializer(serializers.HyperlinkedModelSerializer):

    post_id = serializers.PrimaryKeyRelatedField(
    queryset=Peep.objects.all(),
    source='peep'
    )

    user_id = serializers.ReadOnlyField(source='owner.username')

    peep = serializers.HyperlinkedRelatedField(
        view_name='peep_detail', read_only=True)

    class Meta:
        model = Chirp
        fields = ('text', 'post_id','user_id',
                  'peeps','date')

class PeepSerializer(serializers.HyperlinkedModelSerializer):
    
        # if you want to just return all the JSON reviews in a list for a given restaurant
    chirp = ChirpSerializer(many=True, read_only=True)

        # how to populate the owner field on restaurant data
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Peep
        fields=('id', 'post', 'chirp', 'image', 'date','owner')
