export LOCALES

1_prepare:
	@echo Updating strings locally 1/4
	./update_strings.sh $(LOCALES)

2_push:
	@echo Push strings to Transifex 2/4
	@cd .. && tx push -s

3_pull:
	@echo Pull strings from Transifex 3/4
	@cd .. && tx pull -a

4_compile:
	@echo Compile TS files to QM 4/4
	@for f in $(LOCALES); do lrelease ../resources/i18n/$${f}.ts -qm ../resources/i18n/$${f}.qm; done