import sys
from util.config_loader import ConfigLoader, ConfigError
from etl.extractor import Extractor
from etl.transformer import Transformer
from etl.quality_report_generator import QualityReportGenerator
from etl.loader import Loader
from util.logger import Logger


def main():
    logger = Logger()

    # Load configuration 
    try: 
        config = ConfigLoader().load_config()
    except (ConfigError) as e:
        logger.error(f"Configuration error: {e}")
        sys.exit(1)
    
    # Extract 
    logger.get_logger().info("Starting extract")
    extractor = Extractor(config["extract"])
    data = extractor.extract()
    logger.get_logger().info("Extract finished")
    logger.log_blank_line()

    # Transform
    logger.get_logger().info("Starting transform")
    transformer = Transformer()
    transformed_data = transformer.transform(data)
    logger.get_logger().info("Transform finished")
    logger.log_blank_line()

    # Quality report
    logger.get_logger().info("Generating quality report")
    quality_report_generator = QualityReportGenerator()
    quality_report = quality_report_generator.generate_report(df=transformed_data)
    logger.get_logger().info("Quality report generated")
    logger.log_blank_line()

    # Load
    logger.get_logger().info("Starting load")
    # loader = Loader(config["load"])
    # loader.load(df=transformed_data, quality_report=quality_report)
    logger.get_logger().info("Load finished")

if __name__ == "__main__":
    main()