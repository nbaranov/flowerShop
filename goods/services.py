from goods.models import Product


class ProductService:
    @staticmethod
    def load_many_from_file(file, parser_cls):
        parsed_file = parser_cls.parse(file)
        for row in parsed_file:
            db_product = Product.objects.filter(external_id=row[0])
            if not db_product:
                product = Product.objects.create(
                    external_id=row[0],
                    title=row[1],
                    description=row[2],
                    quantity=row[3],
                    price=row[4]
                )
                product.save()
