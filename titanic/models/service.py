from titanic.models.dataset import Dataset
import pandas as pd


class Service(object):

    dataset = Dataset()

    def new_model(self, payload):
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)


    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis = 1)

    @staticmethod
    def create_lable(this):
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, feature) -> object:
        this.train = this.train.drop([feature], axis = 1)
        this.test = this.test.drop([feature], axis=1)
        return this

    @staticmethod
    def emarked_nominal(this) -> object:
        this.train = this.train.fillna({'Embarked':'S'})
        this.test = this.test.fillna({'Embarked':'S'})
        this.train["Embarked"] = this.train["Embarked"].map({'S':1, 'C':2, 'Q':3})
        this.test["Embarked"] = this.test["Embarked"].map({'S': 1, 'C': 2, 'Q': 3})
        return this

    @staticmethod
    def fare_band_fill_na(this) -> object:
        return this

    @staticmethod
    def title_norminal(this) -> object:
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
        for dataset in combine:
            dataset['Title'] = dataset['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona'], 'Rare')
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Mlle', 'Mr')
            dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] = dataset['Title'].replace('Mme', 'Rare')
            dataset['Title'] = dataset['Title'].fillna({'Title': '0'})
            dataset['Title'] = dataset['Title'].map({'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6})

        return this

    @staticmethod
    def gender_norminal(this) -> object:
        combine = [this.train, this.test]
        gender_mapping = {'male': 0, 'female': 1}

        for i in combine:
            i['Gender'] = i['Sex'].map(gender_mapping)

        return this

    @staticmethod
    def age_ordinal(this) -> object:
        return this

    @staticmethod
    def create_k_fold(this) -> object:
        return

