export LOCALES
export PLUGINNAME

help:
	@echo Run tests inside Docker
	@echo make docker_test
	@echo
	@echo Using translation Makefile commands
	@echo make i18n_1_prepare : To get strings in TS files
	@echo make i18n_2_push : To push strings to Transifex
	@echo make i18n_3_pull : To pull strings from Transifex
	@echo make i18n_4_compile : To compile TS to QM files
	@echo
	@echo Deploy plugin
	@echo make deploy_zip : To generate the ZIP file
	@echo make deploy_upload : To upload the ZIP on plugins.qgis.org

docker_test:
	@echo Running tests inside $(PLUGINNAME)
	@docker stop qgis-testing-environment
	@docker rm qgis-testing-environment
	@docker run -d --name qgis-testing-environment -v ${PWD}:/$(PLUGINNAME) -e DISPLAY=:99 qgis/qgis:release-3_4
	@sleep 10
	@docker exec -it qgis-testing-environment sh -c "qgis_setup.sh $(PLUGINNAME)"
	@docker exec -it qgis-testing-environment sh -c "qgis_testrunner.sh $(PLUGINNAME).test_runner.test_package"
	@status=$?
	@docker stop qgis-testing-environment
	@docker rm qgis-testing-environment
	@exit ${status}

deploy_zip:
	@echo
	@echo "------------------------------------"
	@echo "Exporting plugin to zip package.	"
	@echo "------------------------------------"
	@rm -f ../$(PLUGINNAME).zip
	@git-archive-all --prefix=$(PLUGINNAME)/ ../$(PLUGINNAME).zip
	@echo "Created package: $(PLUGINNAME).zip"

deploy_upload:
	@echo "Not yet implemented"

i18n_1_prepare:
	@echo Updating strings locally 1/4
	./update_strings.sh $(LOCALES)

i18n_2_push:
	@echo Push strings to Transifex 2/4
	@cd .. && tx push -s

i18n_3_pull:
	@echo Pull strings from Transifex 3/4
	@cd .. && tx pull -a

i18n_4_compile:
	@echo Compile TS files to QM 4/4
	@for f in $(LOCALES); do lrelease ../resources/i18n/$${f}.ts -qm ../resources/i18n/$${f}.qm; done
