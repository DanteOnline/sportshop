import graphene
from graphene_django import DjangoObjectType
from sport_equipment.models import Equipment, Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name', 'equipment_set')


class EquipmentType(DjangoObjectType):
    class Meta:
        model = Equipment
        fields = ("id", "name", 'cost', 'category')


class Query(graphene.ObjectType):
    equipment_all = graphene.List(EquipmentType)
    category_all = graphene.List(CategoryType)
    equipment_by_name = graphene.List(EquipmentType, name=graphene.String(required=True))
    category_by_id = graphene.Field(CategoryType, id=graphene.Int(required=True))

    def resolve_equipment_all(self, response):
        return Equipment.objects.all()

    def resolve_category_all(self, response):
        return Category.objects.all()

    def resolve_equipment_by_name(self, response, name):
        return Equipment.objects.filter(name__contains=name)

    def resolve_category_by_id(self, response, id):
        return Category.objects.get(id=id)


class CategoryMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        name = graphene.String(required=True)
        id = graphene.ID()

    # The class attributes define the response of the mutation
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name, id):
        category = Category.objects.get(pk=id)
        category.name = name
        category.save()
        # Notice we return an instance of this mutation
        return CategoryMutation(category=category)


class Mutation(graphene.ObjectType):
    update_category = CategoryMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)