from titanic.models.dataset import Dataset
from titanic.models.service import Service
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns
rc('font', family = font_manager.FontProperties(fname='C:\\Windows\\Fonts\\H2GTRE.ttf').get_name())


class Plot(object):

    dataset: object = Dataset()
    service: object = Service()

    def __init__(self, fname):
        self.entity = self.service.new_model(fname)


    def draw_servived_dead(self):
        this = self.entity
        #print(f'The data type of Train is {type(this)}.')
        #print(f'Columns of Train is {this.columns}.')
        #print(f'The top 5 superior data are {this.head}.')
        #print(f'The top 5 inferior data are {this.tail}.')
        f, ax = plt.subplots(1, 2, figsize = (18, 8))
        this['Survived'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        ax[0].set_title('0.사망자 vs 1.생존자')
        ax[0].set_ylabel('')
        ax[1].set_title('0.사망자 vs 1.생존자')
        sns.countplot('Survived', data=this, ax=ax[1])
        plt.show()

    def draw_Pclass(self):
        this = self.entity
        this['Survived(humanized)'] = this['Survived'].replace(0, "Perish").replace(1, 'Survived')
        this['Pclass(humanized)'] = this['Pclass'].replace(1, 'First Class').replace(2, 'Business').replace(3, 'Economy')
        sns.countplot(data=this, x='Pclass(humanized)', hue='Survived(humanized)')
        plt.show()

    def draw_sex(self):
        this = self.entity
        f, ax = plt.subplots(1, 2, figsize = (18, 8))
        this['Survived'][this['Sex'] == 'male'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        this['Survived'][this['Sex'] == 'female'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[1], shadow=True)

        ax[0].set_title('남성의 생존비율 [0.사망자 vs 1.생존자]')
        ax[1].set_title('여성의 생존비율 [0.사망자 vs 1.생존자]')
        plt.show()

    def draw_embarked(self):
        this = self.entity
        this['Survived(humanized)'] = this['Survived'].replace(0, "Perish").replace(1, 'Survived')
        this['Embarked(humanized)'] = this['Embarked'].replace('C', 'Cherbourg').replace('S', 'Southampton').replace('Q', 'Qeenstown')
        sns.countplot(data=this, x='Embarked(humanized)', hue='Survived(humanized)')
        plt.show()

    def draw_age(self):
        this = self.entity
        this['Survived(humanized)'] = this['Survived'].replace(0, "Perish").replace(1, 'Survived')
        this['age(humanized)'] = this['Age'].replace(range(0, 20), 'boy').replace(range(20,60), 'mr').replace(range(60,100), 'grand')
        sns.countplot(data=this, x='age(humanized)', hue='Survived(humanized)')
        plt.show()


'''
Train 의 type 은 <class 'pandas.core.frame.DataFrame'> 이다
Train 의 column 은 Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
      dtype='object') 이다
Train 의 상위 5개 데이터는    PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns] 이다
Train 의 하위 5개 데이터는      PassengerId  Survived  Pclass  ...   Fare Cabin  Embarked
886          887         0       2  ...  13.00   NaN         S
887          888         1       1  ...  30.00   B42         S
888          889         0       3  ...  23.45   NaN         S
889          890         1       1  ...  30.00  C148         C
890          891         0       3  ...   7.75   NaN         Q
'''



