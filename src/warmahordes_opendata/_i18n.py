import oslo_i18n

DOMAIN = "warmahordes_opendata"

oslo_i18n.enable_lazy()

_translators = oslo_i18n.TranslatorFactory(domain=DOMAIN)

_ = _translators.primary
