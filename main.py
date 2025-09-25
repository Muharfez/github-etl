from util.config_loader import load_config
from etl.extract import Extractor
from etl.transform import Transformer
from etl.load import Loader


def main():
    config = load_config()

    # Extract 
    extractor = Extractor()
    data = extractor.extract(config["extract"])

    # Transform
    transformer = Transformer()
    transformedData = transformer.transform(data)

    # Load
    loader = Loader()
    loader.load(transformedData, config["load"])


if __name__ == "__main__":
    main()