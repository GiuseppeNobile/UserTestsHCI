from django.test import TestCase
from .models import *


class DomandaTest(TestCase):

    def creaDomanda(self):
        Domanda.objects.create(name='domanda01', testoDomanda='come ti chiami?')

    def getDomanda(self):
        domanda01 = Domanda.objects.get(testoDomanda='come ti chiami?')
        self.assertEqual(domanda01.testoDomanda, 'come ti chiami?')


class RispostaTest(TestCase):

    def setUp(self):
        risposta01 = Risposta.objects.create(listaTipi='rispostabreve')

    def testTipo(self):
        risposta01 = Risposta.objects.create(listaTipi='rispostabreve')
        risposta01.scegliTipo()
        self.assertEqual(risposta01.__class__.__name__, 'Risposta')


class RispostaBreveTest(TestCase):

    risposta02 = RispostaBreve.objects.create(risposta='mi chiamo Giuseppe')

    def getRispostaBreve(self):
        risposta02 = RispostaBreve.objects.get(risposta='mi chiamo Giuseppe')
        self.assertEqual(risposta02.risposta, 'mi chiamo Giuseppe')
        self.assertEqual(risposta02.__class__.__name__, 'RispostaBreve')


class RispostaParagrafoTest(TestCase):

    risposta03 = RispostaBreve.objects.create(risposta='AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

    def getRispostaParagrafo(self):
        risposta02 = RispostaBreve.objects.get(risposta='AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        self.assertEqual(risposta02.risposta, 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        self.assertEqual(risposta02.__class__.__name__, 'RispostaParagrafo')


class QuesitoTest(TestCase):

    quesito01 = Quesito.objects.create(testoQuesito='come ti chiami?', risposta='giuseppe')

    def getQuesito(self):
        quesito01 = Quesito.objects.get(Quesito.testoQuesito, Quesito.risposta)
        self.assertEqual(quesito01.testoQuesito, 'come ti chiami?')
        self.assertEqual(quesito01.risposta, 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        self.assertEqual(quesito01.__class__.__name__, 'Quesito')
