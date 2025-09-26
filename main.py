from util.config_loader import load_config
from etl.extractor import Extractor
from etl.transformer import Transformer
from etl.quality_report_generator import QualityReportGenerator
from etl.loader import Loader


def main():
    config = load_config()
    # Extract 
    extractor = Extractor(config["extract"])
    data = extractor.extract()

    # Transform
    transformer = Transformer()
    transformed_data = transformer.transform(data)

    # Quality report
    quality_report_generator = QualityReportGenerator()
    quality_report = quality_report_generator.generate_report(df=transformed_data)

    # Load
    loader = Loader(config["load"])
    loader.load(df=transformed_data, quality_report=quality_report)

if __name__ == "__main__":
    main()