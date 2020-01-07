from traits import Trait

# good_traits these should really be json that is read :D

ritarillinen = Trait("Ritarillinen", "Hahmosi on aina haaveillut olevansa ritari ja on hyvin ritarillinen. +1 MT, Taito - Miekkailu - 3 tasoa.")
ritarillinen.add_effect_to_trait("KUN", 1)

keisarin_suojelus = Trait("Keisarinnan suojelus", "Hahmosi on erityisesti keisarinnan suojeluksessa. Kerran päivässä kun olet ottamassassa yli 5 pistettä vahinkoa voit heittää itensiteettiä suojataksesi itsesi.")

list_of_good_traits = [ritarillinen, keisarin_suojelus]

'''
This is legacy :D
list_of_good_traits = [
    Trait("Ritarillinen", "Hahmosi on aina haaveillut olevansa ritari ja on hyvin ritarillinen. +1 MT, Taito - Miekkailu - 3 tasoa."),
    Trait("Keisarinnan suojelus", "Hahmosi on erityisesti keisarinnan suojeluksessa. Kerran päivässä kun olet ottamassassa yli 5 pistettä vahinkoa voit heittää itensiteettiä suojataksesi itsesi."),
    Trait("Hodor", "HODOR, +4 KUN, +6 KOK, -2 KET, -4 ÄLY, -4 VET, HODOR!, osaat pitää ovia kiinni maagisen hyvin."),
    Trait("Sankarten Veri", "Veressäsi virtaa Avalonin muinaisten sankarien veri, +2 MT."),
    Trait("Lohikäärmeen surma","Olet syntynyt lohikäärmeen surmaajaksi! Harmi vaan että tähdissä niitä ei ole monta. +10 osumiseen suuria hirviöitä kohtaan. Crit 1-11. Olet peloton suuria mörköjä kohtaan."),
    Trait("Business as Usual", "Jotenkin osaat hartiaa kohauttuaen kohdata galaxin kauhut. Itensiteettillä väistät traumavahingon."),
]
'''


list_of_bad_traits = [

]
