import os

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def create_file(path):
    with open(path, 'w') as f:
        pass  # Creates an empty file

def create_project_structure():
    # Root level directories and files
    root_dirs = ['api-gateway', 'data-collector', 'data-processor', 'model-trainer', 
                 'inferencer', 'trader', 'web-interface', 'common', 'tests', 'docs', 
                 'deployment', 'scripts']
    
    root_files = ['.gitignore', 'README.md', 'requirements.txt']

    for dir in root_dirs:
        create_directory(dir)

    for file in root_files:
        create_file(file)

    # Common structure for microservices
    microservices = ['api-gateway', 'data-collector', 'data-processor', 'model-trainer', 
                     'inferencer', 'trader', 'web-interface']
    
    for service in microservices:
        create_file(os.path.join(service, 'main.py'))
        create_file(os.path.join(service, 'requirements.txt'))
        create_file(os.path.join(service, 'Dockerfile'))
        create_directory(os.path.join(service, 'config'))
        create_file(os.path.join(service, 'config', '__init__.py'))
        create_file(os.path.join(service, 'config', 'settings.py'))

    # API Gateway specific
    create_directory(os.path.join('api-gateway', 'routes'))
    create_directory(os.path.join('api-gateway', 'middlewares'))
    routes = ['__init__.py', 'data_routes.py', 'model_routes.py', 'inference_routes.py', 
              'trade_routes.py', 'dashboard_routes.py']
    middlewares = ['__init__.py', 'auth_middleware.py', 'logging_middleware.py']
    
    for route in routes:
        create_file(os.path.join('api-gateway', 'routes', route))
    for middleware in middlewares:
        create_file(os.path.join('api-gateway', 'middlewares', middleware))

    # Data Collector specific
    create_directory(os.path.join('data-collector', 'collectors'))
    create_directory(os.path.join('data-collector', 'models'))
    collectors = ['__init__.py', 'market_data_collector.py', 'historical_data_collector.py']
    for collector in collectors:
        create_file(os.path.join('data-collector', 'collectors', collector))
    create_file(os.path.join('data-collector', 'models', '__init__.py'))
    create_file(os.path.join('data-collector', 'models', 'data_models.py'))

    # Data Processor specific
    create_directory(os.path.join('data-processor', 'processors'))
    create_directory(os.path.join('data-processor', 'features'))
    processors = ['__init__.py', 'data_cleaner.py', 'feature_extractor.py']
    features = ['__init__.py', 'technical_indicators.py', 'fundamental_features.py']
    for processor in processors:
        create_file(os.path.join('data-processor', 'processors', processor))
    for feature in features:
        create_file(os.path.join('data-processor', 'features', feature))

    # Model Trainer specific
    create_directory(os.path.join('model-trainer', 'models'))
    create_directory(os.path.join('model-trainer', 'trainers'))
    create_directory(os.path.join('model-trainer', 'utils'))
    models = ['__init__.py', 'lstm_model.py', 'a3c_model.py']
    trainers = ['__init__.py', 'lstm_trainer.py', 'a3c_trainer.py']
    for model in models:
        create_file(os.path.join('model-trainer', 'models', model))
    for trainer in trainers:
        create_file(os.path.join('model-trainer', 'trainers', trainer))
    create_file(os.path.join('model-trainer', 'utils', '__init__.py'))
    create_file(os.path.join('model-trainer', 'utils', 'data_loader.py'))

    # Inferencer specific
    create_directory(os.path.join('inferencer', 'models'))
    create_directory(os.path.join('inferencer', 'predictors'))
    create_file(os.path.join('inferencer', 'models', '__init__.py'))
    create_file(os.path.join('inferencer', 'models', 'model_loader.py'))
    create_file(os.path.join('inferencer', 'predictors', '__init__.py'))
    create_file(os.path.join('inferencer', 'predictors', 'predictor.py'))

    # Trader specific
    create_directory(os.path.join('trader', 'executors'))
    create_directory(os.path.join('trader', 'strategies'))
    create_directory(os.path.join('trader', 'models'))
    create_file(os.path.join('trader', 'executors', '__init__.py'))
    create_file(os.path.join('trader', 'executors', 'order_executor.py'))
    create_file(os.path.join('trader', 'strategies', '__init__.py'))
    create_file(os.path.join('trader', 'strategies', 'trading_strategy.py'))
    create_file(os.path.join('trader', 'models', '__init__.py'))
    create_file(os.path.join('trader', 'models', 'order_models.py'))

    # Web Interface specific
    create_directory(os.path.join('web-interface', 'static'))
    create_directory(os.path.join('web-interface', 'static', 'css'))
    create_directory(os.path.join('web-interface', 'static', 'js'))
    create_directory(os.path.join('web-interface', 'static', 'img'))
    create_directory(os.path.join('web-interface', 'templates'))
    create_directory(os.path.join('web-interface', 'routes'))
    create_file(os.path.join('web-interface', 'static', 'css', 'styles.css'))
    create_file(os.path.join('web-interface', 'static', 'js', 'dashboard.js'))
    create_file(os.path.join('web-interface', 'static', 'js', 'charts.js'))
    create_file(os.path.join('web-interface', 'static', 'img', 'logo.png'))
    templates = ['base.html', 'dashboard.html', 'settings.html', 'logs.html']
    for template in templates:
        create_file(os.path.join('web-interface', 'templates', template))
    create_file(os.path.join('web-interface', 'routes', '__init__.py'))
    create_file(os.path.join('web-interface', 'routes', 'dashboard_routes.py'))
    create_file(os.path.join('web-interface', 'routes', 'api_routes.py'))

    # Common directory
    common_files = ['__init__.py', 'database.py', 'logger.py', 'utils.py', 'exceptions.py']
    for file in common_files:
        create_file(os.path.join('common', file))

    # Tests directory
    create_directory(os.path.join('tests', 'unit'))
    create_directory(os.path.join('tests', 'integration'))
    unit_tests = ['test_data_collector.py', 'test_data_processor.py', 'test_model_trainer.py', 
                  'test_inferencer.py', 'test_trader.py']
    integration_tests = ['test_data_pipeline.py', 'test_model_pipeline.py', 'test_trading_pipeline.py']
    for test in unit_tests:
        create_file(os.path.join('tests', 'unit', test))
    for test in integration_tests:
        create_file(os.path.join('tests', 'integration', test))

    # Docs directory
    docs = ['api_docs.md', 'architecture.md', 'setup_guide.md', 'user_manual.md']
    for doc in docs:
        create_file(os.path.join('docs', doc))

    # Deployment directory
    create_file(os.path.join('deployment', 'docker-compose.yml'))
    create_file(os.path.join('deployment', 'nginx.conf'))
    create_directory(os.path.join('deployment', 'kubernetes'))
    k8s_files = ['api-gateway-deployment.yaml', 'data-collector-deployment.yaml', 
                 'data-processor-deployment.yaml', 'model-trainer-deployment.yaml', 
                 'inferencer-deployment.yaml', 'trader-deployment.yaml', 'web-interface-deployment.yaml']
    for file in k8s_files:
        create_file(os.path.join('deployment', 'kubernetes', file))

    # Scripts directory
    scripts = ['setup.sh', 'run_tests.sh', 'deploy.sh']
    for script in scripts:
        create_file(os.path.join('scripts', script))

if __name__ == "__main__":
    create_project_structure()
    print("Project structure created successfully!")