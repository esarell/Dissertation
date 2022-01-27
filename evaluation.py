from kiwi.lib.evaluate import evaluate_from_configuration
from kiwi.lib.utils import file_to_configuration

configuration_dict = file_to_configuration('config/evaluate.yaml')
report = evaluate_from_configuration(configuration_dict)
print(report)
