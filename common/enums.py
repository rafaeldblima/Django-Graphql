from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def valores(cls):
        return [x.value for x in cls]

    @classmethod
    def valores_enum(cls):
        return [x for x in cls]

    @classmethod
    def valor_by_prop(cls, prop, val):
        valores_filtrados = [x for x in cls if getattr(x, prop) == val]
        return valores_filtrados[0] if valores_filtrados else None

    @classmethod
    def valor_por_indice(cls, indice):
        valores = cls.valores_enum()
        return valores[indice] if len(valores) > 0 else None

    def ordinal(self):
        return self.valores().index(self.value)
