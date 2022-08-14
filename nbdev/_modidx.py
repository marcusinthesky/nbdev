# Autogenerated by nbdev

d = { 'settings': { 'allowed_cell_metadata_keys': '',
                'allowed_metadata_keys': '',
                'audience': 'Developers',
                'author': 'Jeremy Howard and Hamel Husain',
                'author_email': 'j@fast.ai',
                'black_formatting': 'False',
                'branch': 'master',
                'clean_ids': 'True',
                'conda_requirements': 'pyyaml',
                'conda_user': 'fastai',
                'console_scripts': 'nbdev_create_config=nbdev.read:nbdev_create_config\n'
                                   'nbdev_update=nbdev.sync:nbdev_update\n'
                                   'nbdev_export=nbdev.doclinks:nbdev_export\n'
                                   'nbdev_fix=nbdev.merge:nbdev_fix\n'
                                   'nbdev_merge=nbdev.merge:nbdev_merge\n'
                                   'nbdev_trust=nbdev.clean:nbdev_trust\n'
                                   'nbdev_clean=nbdev.clean:nbdev_clean\n'
                                   'nbdev_install_hooks=nbdev.clean:nbdev_install_hooks\n'
                                   'nbdev_filter=nbdev.cli:nbdev_filter\n'
                                   'nbdev_quarto=nbdev.cli:nbdev_quarto\n'
                                   'nbdev_sidebar=nbdev.cli:nbdev_sidebar\n'
                                   'nbdev_test=nbdev.test:nbdev_test\n'
                                   'nbdev_bump_version=nbdev.cli:nbdev_bump_version\n'
                                   'nbdev_new=nbdev.cli:nbdev_new\n'
                                   'nbdev_migrate=nbdev.migrate:nbdev_migrate\n'
                                   'nbdev_install_quarto=nbdev.cli:install_quarto\n'
                                   'nbdev_install=nbdev.cli:install\n'
                                   'nbdev_docs=nbdev.cli:nbdev_quarto\n'
                                   'nbdev_preview=nbdev.cli:preview\n'
                                   'nbdev_deploy=nbdev.cli:deploy\n'
                                   'nbdev_prepare=nbdev.cli:prepare\n'
                                   'nbdev_readme=nbdev.cli:nbdev_readme\n'
                                   'nbdev_release_gh=nbdev.release:release_gh\n'
                                   'nbdev_release_git=nbdev.release:release_git\n'
                                   'nbdev_changelog=nbdev.release:changelog\n'
                                   'nbdev_pypi=nbdev.release:release_pypi\n'
                                   'nbdev_conda=nbdev.release:release_conda\n'
                                   'nbdev_release_both=nbdev.release:release_both\n'
                                   'nbdev_help=nbdev.cli:chelp',
                'copyright': '2020 onwards, Jeremy Howard',
                'custom_quarto_yml': 'False',
                'custom_sidebar': 'True',
                'description': 'Create delightful software with Jupyter Notebooks',
                'dev_requirements': 'nbdev-numpy nbdev-stdlib pandas matplotlib black',
                'doc_baseurl': '/',
                'doc_host': 'https://nbdev.fast.ai',
                'doc_path': '_docs',
                'git_url': 'https://github.com/fastai/nbdev',
                'jupyter_hooks': 'True',
                'keywords': 'nbdev fastai jupyter notebook export',
                'language': 'English',
                'lib_name': 'nbdev',
                'lib_path': 'nbdev',
                'license': 'apache2',
                'min_python': '3.7',
                'nbs_path': 'nbs',
                'pip_requirements': 'PyYAML',
                'readme_nb': 'getting_started.ipynb',
                'recursive': 'False',
                'requirements': 'fastcore>=1.5.17 execnb>=0.0.10 astunparse ghapi',
                'status': '2',
                'title': 'nbdev',
                'tst_flags': 'notest',
                'user': 'fastai',
                'version': '2.2.0'},
  'syms': { 'nbdev.clean': { 'nbdev.clean.clean_jupyter': 'https://nbdev.fast.ai/clean.html#clean_jupyter',
                             'nbdev.clean.clean_nb': 'https://nbdev.fast.ai/clean.html#clean_nb',
                             'nbdev.clean.nbdev_clean': 'https://nbdev.fast.ai/clean.html#nbdev_clean',
                             'nbdev.clean.nbdev_install_hooks': 'https://nbdev.fast.ai/clean.html#nbdev_install_hooks',
                             'nbdev.clean.nbdev_trust': 'https://nbdev.fast.ai/clean.html#nbdev_trust',
                             'nbdev.clean.process_write': 'https://nbdev.fast.ai/clean.html#process_write'},
            'nbdev.cli': { 'nbdev.cli.BASE_QUARTO_URL': 'https://nbdev.fast.ai/cli.html#base_quarto_url',
                           'nbdev.cli.FilterDefaults': 'https://nbdev.fast.ai/cli.html#filterdefaults',
                           'nbdev.cli.FilterDefaults.base_postprocs': 'https://nbdev.fast.ai/cli.html#filterdefaults.base_postprocs',
                           'nbdev.cli.FilterDefaults.base_preprocs': 'https://nbdev.fast.ai/cli.html#filterdefaults.base_preprocs',
                           'nbdev.cli.FilterDefaults.base_procs': 'https://nbdev.fast.ai/cli.html#filterdefaults.base_procs',
                           'nbdev.cli.FilterDefaults.nb_proc': 'https://nbdev.fast.ai/cli.html#filterdefaults.nb_proc',
                           'nbdev.cli.FilterDefaults.postprocs': 'https://nbdev.fast.ai/cli.html#filterdefaults.postprocs',
                           'nbdev.cli.FilterDefaults.preprocs': 'https://nbdev.fast.ai/cli.html#filterdefaults.preprocs',
                           'nbdev.cli.FilterDefaults.procs': 'https://nbdev.fast.ai/cli.html#filterdefaults.procs',
                           'nbdev.cli.bump_version': 'https://nbdev.fast.ai/cli.html#bump_version',
                           'nbdev.cli.chelp': 'https://nbdev.fast.ai/cli.html#chelp',
                           'nbdev.cli.deploy': 'https://nbdev.fast.ai/cli.html#deploy',
                           'nbdev.cli.extract_tgz': 'https://nbdev.fast.ai/cli.html#extract_tgz',
                           'nbdev.cli.install': 'https://nbdev.fast.ai/cli.html#install',
                           'nbdev.cli.install_quarto': 'https://nbdev.fast.ai/cli.html#install_quarto',
                           'nbdev.cli.nbdev_bump_version': 'https://nbdev.fast.ai/cli.html#nbdev_bump_version',
                           'nbdev.cli.nbdev_filter': 'https://nbdev.fast.ai/cli.html#nbdev_filter',
                           'nbdev.cli.nbdev_new': 'https://nbdev.fast.ai/cli.html#nbdev_new',
                           'nbdev.cli.nbdev_quarto': 'https://nbdev.fast.ai/cli.html#nbdev_quarto',
                           'nbdev.cli.nbdev_readme': 'https://nbdev.fast.ai/cli.html#nbdev_readme',
                           'nbdev.cli.nbdev_sidebar': 'https://nbdev.fast.ai/cli.html#nbdev_sidebar',
                           'nbdev.cli.prepare': 'https://nbdev.fast.ai/cli.html#prepare',
                           'nbdev.cli.preview': 'https://nbdev.fast.ai/cli.html#preview',
                           'nbdev.cli.prompt_user': 'https://nbdev.fast.ai/cli.html#prompt_user',
                           'nbdev.cli.refresh_quarto_yml': 'https://nbdev.fast.ai/cli.html#refresh_quarto_yml'},
            'nbdev.doclinks': { 'nbdev.doclinks.DocLinks': 'https://nbdev.fast.ai/doclinks.html#doclinks',
                                'nbdev.doclinks.DocLinks.build_index': 'https://nbdev.fast.ai/doclinks.html#doclinks.build_index',
                                'nbdev.doclinks.DocLinks.update_syms': 'https://nbdev.fast.ai/doclinks.html#doclinks.update_syms',
                                'nbdev.doclinks.DocLinks.write_nbdev_idx': 'https://nbdev.fast.ai/doclinks.html#doclinks.write_nbdev_idx',
                                'nbdev.doclinks.NbdevLookup': 'https://nbdev.fast.ai/doclinks.html#nbdevlookup',
                                'nbdev.doclinks.NbdevLookup._link_sym': 'https://nbdev.fast.ai/doclinks.html#nbdevlookup._link_sym',
                                'nbdev.doclinks.NbdevLookup.link_line': 'https://nbdev.fast.ai/doclinks.html#nbdevlookup.link_line',
                                'nbdev.doclinks.NbdevLookup.linkify': 'https://nbdev.fast.ai/doclinks.html#nbdevlookup.linkify',
                                'nbdev.doclinks.build_modidx': 'https://nbdev.fast.ai/doclinks.html#build_modidx',
                                'nbdev.doclinks.get_patch_name': 'https://nbdev.fast.ai/doclinks.html#get_patch_name',
                                'nbdev.doclinks.nbdev_export': 'https://nbdev.fast.ai/doclinks.html#nbdev_export',
                                'nbdev.doclinks.nbglob': 'https://nbdev.fast.ai/doclinks.html#nbglob'},
            'nbdev.export': { 'nbdev.export.ExportModuleProc': 'https://nbdev.fast.ai/export.html#exportmoduleproc',
                              'nbdev.export.black_format': 'https://nbdev.fast.ai/export.html#black_format',
                              'nbdev.export.create_modules': 'https://nbdev.fast.ai/export.html#create_modules',
                              'nbdev.export.nb_export': 'https://nbdev.fast.ai/export.html#nb_export'},
            'nbdev.extract_attachments': { 'nbdev.extract_attachments.ExtractAttachmentsPreprocessor': 'https://nbdev.fast.ai/extract_attachments.html#extractattachmentspreprocessor',
                                           'nbdev.extract_attachments.ExtractAttachmentsPreprocessor.preprocess_cell': 'https://nbdev.fast.ai/extract_attachments.html#extractattachmentspreprocessor.preprocess_cell'},
            'nbdev.imports': {},
            'nbdev.maker': { 'nbdev.maker.ModuleMaker': 'https://nbdev.fast.ai/maker.html#modulemaker',
                             'nbdev.maker.ModuleMaker._last_future': 'https://nbdev.fast.ai/maker.html#modulemaker._last_future',
                             'nbdev.maker.ModuleMaker._make_exists': 'https://nbdev.fast.ai/maker.html#modulemaker._make_exists',
                             'nbdev.maker.ModuleMaker._update_all': 'https://nbdev.fast.ai/maker.html#modulemaker._update_all',
                             'nbdev.maker.ModuleMaker.make': 'https://nbdev.fast.ai/maker.html#modulemaker.make',
                             'nbdev.maker.ModuleMaker.make_all': 'https://nbdev.fast.ai/maker.html#modulemaker.make_all',
                             'nbdev.maker.NbCell.import2relative': 'https://nbdev.fast.ai/maker.html#nbcell.import2relative',
                             'nbdev.maker.basic_export_nb2': 'https://nbdev.fast.ai/maker.html#basic_export_nb2',
                             'nbdev.maker.decor_id': 'https://nbdev.fast.ai/maker.html#decor_id',
                             'nbdev.maker.find_var': 'https://nbdev.fast.ai/maker.html#find_var',
                             'nbdev.maker.make_code_cells': 'https://nbdev.fast.ai/maker.html#make_code_cells',
                             'nbdev.maker.read_var': 'https://nbdev.fast.ai/maker.html#read_var',
                             'nbdev.maker.relative_import': 'https://nbdev.fast.ai/maker.html#relative_import',
                             'nbdev.maker.retr_exports': 'https://nbdev.fast.ai/maker.html#retr_exports',
                             'nbdev.maker.update_import': 'https://nbdev.fast.ai/maker.html#update_import',
                             'nbdev.maker.update_var': 'https://nbdev.fast.ai/maker.html#update_var'},
            'nbdev.merge': { 'nbdev.merge.conf_re': 'https://nbdev.fast.ai/merge.html#conf_re',
                             'nbdev.merge.nbdev_fix': 'https://nbdev.fast.ai/merge.html#nbdev_fix',
                             'nbdev.merge.nbdev_merge': 'https://nbdev.fast.ai/merge.html#nbdev_merge',
                             'nbdev.merge.unpatch': 'https://nbdev.fast.ai/merge.html#unpatch'},
            'nbdev.migrate': { 'nbdev.migrate.migrate_md_fm': 'https://nbdev.fast.ai/migrate.html#migrate_md_fm',
                               'nbdev.migrate.migrate_nb_fm': 'https://nbdev.fast.ai/migrate.html#migrate_nb_fm',
                               'nbdev.migrate.nbdev_migrate': 'https://nbdev.fast.ai/migrate.html#nbdev_migrate'},
            'nbdev.mkdocs': { 'nbdev.mkdocs.RmNumPrefix': 'https://nbdev.fast.ai/mkdocs.html#rmnumprefix',
                              'nbdev.mkdocs.RmNumPrefix.on_pre_page': 'https://nbdev.fast.ai/mkdocs.html#rmnumprefix.on_pre_page'},
            'nbdev.process': { 'nbdev.process.NBProcessor': 'https://nbdev.fast.ai/process.html#nbprocessor',
                               'nbdev.process.NBProcessor.process': 'https://nbdev.fast.ai/process.html#nbprocessor.process',
                               'nbdev.process.extract_directives': 'https://nbdev.fast.ai/process.html#extract_directives',
                               'nbdev.process.first_code_ln': 'https://nbdev.fast.ai/process.html#first_code_ln',
                               'nbdev.process.instantiate': 'https://nbdev.fast.ai/process.html#instantiate',
                               'nbdev.process.langs': 'https://nbdev.fast.ai/process.html#langs',
                               'nbdev.process.nb_lang': 'https://nbdev.fast.ai/process.html#nb_lang',
                               'nbdev.process.opt_set': 'https://nbdev.fast.ai/process.html#opt_set'},
            'nbdev.processors': { 'nbdev.processors.add_links': 'https://nbdev.fast.ai/processors.html#add_links',
                                  'nbdev.processors.add_show_docs': 'https://nbdev.fast.ai/processors.html#add_show_docs',
                                  'nbdev.processors.cell_lang': 'https://nbdev.fast.ai/processors.html#cell_lang',
                                  'nbdev.processors.clean_magics': 'https://nbdev.fast.ai/processors.html#clean_magics',
                                  'nbdev.processors.clean_show_doc': 'https://nbdev.fast.ai/processors.html#clean_show_doc',
                                  'nbdev.processors.construct_fm': 'https://nbdev.fast.ai/processors.html#construct_fm',
                                  'nbdev.processors.exec_show_docs': 'https://nbdev.fast.ai/processors.html#exec_show_docs',
                                  'nbdev.processors.filter_fm': 'https://nbdev.fast.ai/processors.html#filter_fm',
                                  'nbdev.processors.filter_stream_': 'https://nbdev.fast.ai/processors.html#filter_stream_',
                                  'nbdev.processors.hide_': 'https://nbdev.fast.ai/processors.html#hide_',
                                  'nbdev.processors.hide_line': 'https://nbdev.fast.ai/processors.html#hide_line',
                                  'nbdev.processors.infer_frontmatter': 'https://nbdev.fast.ai/processors.html#infer_frontmatter',
                                  'nbdev.processors.insert_frontmatter': 'https://nbdev.fast.ai/processors.html#insert_frontmatter',
                                  'nbdev.processors.insert_warning': 'https://nbdev.fast.ai/processors.html#insert_warning',
                                  'nbdev.processors.is_frontmatter': 'https://nbdev.fast.ai/processors.html#is_frontmatter',
                                  'nbdev.processors.lang_identify': 'https://nbdev.fast.ai/processors.html#lang_identify',
                                  'nbdev.processors.nb_fmdict': 'https://nbdev.fast.ai/processors.html#nb_fmdict',
                                  'nbdev.processors.nbflags_': 'https://nbdev.fast.ai/processors.html#nbflags_',
                                  'nbdev.processors.populate_language': 'https://nbdev.fast.ai/processors.html#populate_language',
                                  'nbdev.processors.rm_export': 'https://nbdev.fast.ai/processors.html#rm_export',
                                  'nbdev.processors.rm_header_dash': 'https://nbdev.fast.ai/processors.html#rm_header_dash',
                                  'nbdev.processors.strip_ansi': 'https://nbdev.fast.ai/processors.html#strip_ansi',
                                  'nbdev.processors.strip_hidden_metadata': 'https://nbdev.fast.ai/processors.html#strip_hidden_metadata',
                                  'nbdev.processors.yaml_str': 'https://nbdev.fast.ai/processors.html#yaml_str',
                                  'nbdev.processors.yml2dict': 'https://nbdev.fast.ai/processors.html#yml2dict'},
            'nbdev.read': { 'nbdev.read.add_init': 'https://nbdev.fast.ai/read.html#add_init',
                            'nbdev.read.basic_export_nb': 'https://nbdev.fast.ai/read.html#basic_export_nb',
                            'nbdev.read.config_key': 'https://nbdev.fast.ai/read.html#config_key',
                            'nbdev.read.create_output': 'https://nbdev.fast.ai/read.html#create_output',
                            'nbdev.read.get_config': 'https://nbdev.fast.ai/read.html#get_config',
                            'nbdev.read.nbdev_create_config': 'https://nbdev.fast.ai/read.html#nbdev_create_config',
                            'nbdev.read.show_src': 'https://nbdev.fast.ai/read.html#show_src',
                            'nbdev.read.update_version': 'https://nbdev.fast.ai/read.html#update_version',
                            'nbdev.read.write_cells': 'https://nbdev.fast.ai/read.html#write_cells'},
            'nbdev.release': { 'nbdev.release.GH_HOST': 'https://nbdev.fast.ai/release.html#gh_host',
                               'nbdev.release.Release': 'https://nbdev.fast.ai/release.html#release',
                               'nbdev.release.Release.changelog': 'https://nbdev.fast.ai/release.html#release.changelog',
                               'nbdev.release.Release.latest_notes': 'https://nbdev.fast.ai/release.html#release.latest_notes',
                               'nbdev.release.Release.release': 'https://nbdev.fast.ai/release.html#release.release',
                               'nbdev.release.anaconda_upload': 'https://nbdev.fast.ai/release.html#anaconda_upload',
                               'nbdev.release.changelog': 'https://nbdev.fast.ai/release.html#changelog',
                               'nbdev.release.chk_conda_rel': 'https://nbdev.fast.ai/release.html#chk_conda_rel',
                               'nbdev.release.conda_output_path': 'https://nbdev.fast.ai/release.html#conda_output_path',
                               'nbdev.release.latest_pypi': 'https://nbdev.fast.ai/release.html#latest_pypi',
                               'nbdev.release.pypi_details': 'https://nbdev.fast.ai/release.html#pypi_details',
                               'nbdev.release.pypi_json': 'https://nbdev.fast.ai/release.html#pypi_json',
                               'nbdev.release.release_both': 'https://nbdev.fast.ai/release.html#release_both',
                               'nbdev.release.release_conda': 'https://nbdev.fast.ai/release.html#release_conda',
                               'nbdev.release.release_gh': 'https://nbdev.fast.ai/release.html#release_gh',
                               'nbdev.release.release_git': 'https://nbdev.fast.ai/release.html#release_git',
                               'nbdev.release.release_pypi': 'https://nbdev.fast.ai/release.html#release_pypi',
                               'nbdev.release.write_conda_meta': 'https://nbdev.fast.ai/release.html#write_conda_meta'},
            'nbdev.showdoc': { 'nbdev.showdoc.BasicHtmlRenderer': 'https://nbdev.fast.ai/showdoc.html#basichtmlrenderer',
                               'nbdev.showdoc.BasicMarkdownRenderer': 'https://nbdev.fast.ai/showdoc.html#basicmarkdownrenderer',
                               'nbdev.showdoc.DocmentTbl': 'https://nbdev.fast.ai/showdoc.html#docmenttbl',
                               'nbdev.showdoc.DocmentTbl.has_docment': 'https://nbdev.fast.ai/showdoc.html#docmenttbl.has_docment',
                               'nbdev.showdoc.DocmentTbl.has_return': 'https://nbdev.fast.ai/showdoc.html#docmenttbl.has_return',
                               'nbdev.showdoc.DocmentTbl.hdr_str': 'https://nbdev.fast.ai/showdoc.html#docmenttbl.hdr_str',
                               'nbdev.showdoc.DocmentTbl.params_str': 'https://nbdev.fast.ai/showdoc.html#docmenttbl.params_str',
                               'nbdev.showdoc.DocmentTbl.return_str': 'https://nbdev.fast.ai/showdoc.html#docmenttbl.return_str',
                               'nbdev.showdoc.ShowDocRenderer': 'https://nbdev.fast.ai/showdoc.html#showdocrenderer',
                               'nbdev.showdoc.colab_link': 'https://nbdev.fast.ai/showdoc.html#colab_link',
                               'nbdev.showdoc.doc': 'https://nbdev.fast.ai/showdoc.html#doc',
                               'nbdev.showdoc.show_doc': 'https://nbdev.fast.ai/showdoc.html#show_doc',
                               'nbdev.showdoc.showdoc_nm': 'https://nbdev.fast.ai/showdoc.html#showdoc_nm'},
            'nbdev.sync': { 'nbdev.sync.absolute_import': 'https://nbdev.fast.ai/sync.html#absolute_import',
                            'nbdev.sync.nbdev_update': 'https://nbdev.fast.ai/sync.html#nbdev_update'},
            'nbdev.test': { 'nbdev.test.nbdev_test': 'https://nbdev.fast.ai/test.html#nbdev_test',
                            'nbdev.test.test_nb': 'https://nbdev.fast.ai/test.html#test_nb'},
            'nbdev.tutorial': { 'nbdev.tutorial.HelloSayer': 'https://nbdev.fast.ai/tutorial.html#hellosayer',
                                'nbdev.tutorial.HelloSayer.say': 'https://nbdev.fast.ai/tutorial.html#hellosayer.say',
                                'nbdev.tutorial.say_hello': 'https://nbdev.fast.ai/tutorial.html#say_hello'}}}