from util.config_loader import load_config
from etl.extractor import Extractor
from etl.transformer import Transformer
from etl.loader import Loader


def main():
    config = load_config()
    # Extract 
    extractor = Extractor(config["extract"])
    data = extractor.extract()

    # Transform
    transformer = Transformer()
    transformedData = transformer.transform(data)

    # Load
    loader = Loader()
    loader.load(transformedData, config["load"])

if __name__ == "__main__":
    main()