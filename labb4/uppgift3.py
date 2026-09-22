import matplotlib.pyplot as plt

categories = ['Vattenkraft', 'Pumpkraft', 'Kärnkraft', 'Vindkraft', 'Solkraft', 'Konventionell värmekraft', 'Import']
data_1983 = [60933, 567, 69951, 0, 0, 3550 + 2896 + 690 + 64, 1835]
data_2023 = [66095, 145, 48470, 34245, 3098, 7327+6500+186+12, 7329]
colors=['blue', 'black', 'purple', 'green', 'yellow', 'orange', 'red']



fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))
fig.suptitle('Kraftslagens fördelning i Sverige')

ax1.set_title('1983')
ax1.pie(data_1983, colors=colors, autopct='%1.1f%%')

ax2.set_title('2023')
ax2.pie(data_2023, colors=colors, autopct='%1.1f%%')

ax2.legend(
    categories,
    title='Kraftslag',
    loc='center left',
    bbox_to_anchor=(1.05, 0.5),
)

plt.tight_layout()
plt.show()