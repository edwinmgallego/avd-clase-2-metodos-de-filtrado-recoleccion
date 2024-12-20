import pandas as pd
import scipy.stats as stats

# Cargar el dataset
df = pd.read_csv('titanic.csv')

# Prueba de hipótesis
survival_by_gender = df.groupby('Sex')['Survived'].mean()
t_stat, p_value = stats.ttest_ind(df[df['Sex'] == 'male']['Survived'], df[df['Sex'] == 'female']['Survived'])
print(f'T-statistic: {t_stat}, P-value: {p_value}')

# ANOVA
anova_result = stats.f_oneway(df[df['Pclass'] == 1]['Age'].dropna(),
                              df[df['Pclass'] == 2]['Age'].dropna(),
                              df[df['Pclass'] == 3]['Age'].dropna())
print(f'ANOVA result: {anova_result}')