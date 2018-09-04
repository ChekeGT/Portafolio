from .models import SocialNetwork


def ctx_dict(request):
    dict = {}
    social_networks = SocialNetwork.objects.all()
    for social_network in social_networks:
        dict[social_network.key] = social_network.url
    return dict