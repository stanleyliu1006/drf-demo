from apps.models import AddressModel
from pactman.verifier.verify import ProviderStateMissing

def provider_state(name, **params):
    if name == 'Stanley':
        Address.objects.create(first_name='Stanley', last_name='Liu', phone='0425 226 866')
    else:
        raise ProviderStateMissing(name)

def test_pacts(live_server, pact_verifier):
    pact_verifier.verify(live_server.url, provider_state)