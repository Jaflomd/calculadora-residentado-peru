#!/usr/bin/env python3
# build.py — genera index.html de la calculadora (v2, bilingüe ES/EN)
# Uso: python3 build.py  (desde calculadora/; lee ../outputs/*.csv)
# Reproducible: para la recalibración anual basta regenerar los CSVs y correr esto.
import pandas as pd, json, unicodedata

c2a = pd.read_csv('../outputs/formula_2a.csv').set_index('variable')['beta'].to_dict()
c2b = pd.read_csv('../outputs/formula_2b.csv').set_index('variable')['beta'].to_dict()
comp = pd.read_csv('../outputs/competitividad_ordinal.csv')

# ---- nombres correctos en español (fix confirmado: tildes, ñ, conectores) ----
ACENTOS = {
 'CIRUGIA':'Cirugía','PEDIATRIA':'Pediatría','GINECOLOGIA':'Ginecología','OBSTETRICIA':'Obstetricia',
 'ORTOPEDIA':'Ortopedia','TRAUMATOLOGIA':'Traumatología','ANESTESIOLOGIA':'Anestesiología',
 'GASTROENTEROLOGIA':'Gastroenterología','RADIOLOGIA':'Radiología','OFTALMOLOGIA':'Oftalmología',
 'DERMATOLOGIA':'Dermatología','PSIQUIATRIA':'Psiquiatría','CARDIOLOGIA':'Cardiología',
 'OTORRINOLARINGOLOGIA':'Otorrinolaringología','MEDICINA':'Medicina','FISICA':'Física',
 'REHABILITACION':'Rehabilitación','ENDOCRINOLOGIA':'Endocrinología','NEUROCIRUGIA':'Neurocirugía',
 'PLASTICA':'Plástica','UROLOGIA':'Urología','INTERNA':'Interna','TORAX':'Tórax',
 'CARDIOVASCULAR':'Cardiovascular','ONCOLOGICA':'Oncológica','INTENSIVA':'Intensiva',
 'NEUROLOGIA':'Neurología','NEFROLOGIA':'Nefrología','NEUMOLOGIA':'Neumología',
 'PEDIATRICA':'Pediátrica','PEDIATRICAS':'Pediátricas','EMERGENCIAS':'Emergencias',
 'DESASTRES':'Desastres','REUMATOLOGIA':'Reumatología','RECONSTRUCTIVA':'Reconstructiva',
 'PATOLOGIA':'Patología','PATOLOGICA':'Patológica','CLINICA':'Clínica','CABEZA':'Cabeza','CUELLO':'Cuello',
 'MAXILOFACIAL':'Maxilofacial','ADMINISTRACION':'Administración','GESTION':'Gestión',
 'SALUD':'Salud','GERIATRIA':'Geriatría','ANATOMIA':'Anatomía','FAMILIAR':'Familiar',
 'COMUNITARIA':'Comunitaria','NEONATOLOGIA':'Neonatología','HEMATOLOGIA':'Hematología',
 'OCUPACIONAL':'Ocupacional','MEDIO':'Medio','AMBIENTE':'Ambiente','ENFERMEDADES':'Enfermedades',
 'INFECCIOSAS':'Infecciosas','TROPICALES':'Tropicales','INMUNOLOGIA':'Inmunología',
 'ALERGIA':'Alergia','RETINA':'Retina','VITREO':'Vítreo','RADIOTERAPIA':'Radioterapia',
 'LEGAL':'Legal','INTERVENCIONISTA':'Intervencionista','NINO':'Niño','ADOLESCENTE':'Adolescente',
 'MANO':'Mano','HEPATOPANCREATOBILIAR':'Hepatopancreatobiliar','TRANSPLANTE':'Trasplante',
 'NUCLEAR':'Nuclear','GENETICA':'Genética','MEDICA':'Médica','DEPORTE':'Deporte',
 'MAMAS':'Mamas','TEJIDOS':'Tejidos','BLANDOS':'Blandos','PIEL':'Piel','COLON':'Colon',
 'RECTO':'Recto','ANO':'Ano','ESTRABISMO':'Estrabismo','ONCOLOGIA':'Oncología',
 'ADICCIONES':'Adicciones','INFECTOLOGIA':'Infectología','ABDOMINAL':'Abdominal',
 'TERAPIA':'Terapia','ADOLESCENTOLOGIA':'Adolescentología','GENERAL':'General',
}
CONECTORES = {'Y':'y','DE':'de','DEL':'del','EN':'en','A':'a','LA':'la','PARA':'para'}

def nombre_es(raw):
    out = []
    for i, w in enumerate(raw.split()):
        if i > 0 and w in CONECTORES: out.append(CONECTORES[w])
        elif w in ACENTOS: out.append(ACENTOS[w])
        else: out.append(w.capitalize())
    return ' '.join(out)

def nivel_key(et):
    return {'Muy alta':'muy_alta','Alta':'alta','Media':'media','Baja':'baja'}[et]

esp = sorted(
    [{"k": r.especialidad, "n": nombre_es(r.especialidad),
      "z": round(r.z_final, 3), "e": nivel_key(r.etiqueta)} for r in comp.itertuples()],
    key=lambda x: unicodedata.normalize('NFD', x["n"]))
sin_acento = [w for x in esp for w in x["k"].split()
              if w not in ACENTOS and w not in CONECTORES]
if sin_acento:
    print('AVISO palabras sin mapa (pasaron por capitalize):', sorted(set(sin_acento)))
DEFAULT_IDX = next(i for i, x in enumerate(esp) if x["k"] == 'CIRUGIA GENERAL')

DATA = json.dumps({"c2a": c2a, "c2b": c2b, "esp": esp}, ensure_ascii=False)

html = open('template.html', encoding='utf-8').read()
html = html.replace('__DATA__', DATA).replace('__DEFAULT_IDX__', str(DEFAULT_IDX))
open('index.html', 'w', encoding='utf-8').write(html)
print(f'index.html v2 generado: {len(esp)} especialidades, default idx {DEFAULT_IDX}')
