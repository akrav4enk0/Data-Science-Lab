import matplotlib.pyplot as plt
import numpy as np

models = ['GLM-4.6', 'Kimi-K2-Thinking', 'DeepSeek-V3.1', 'Kimi-K2-Instruct', 
          'Qwen3-80B', 'Apertus-70B', 'Apertus-8B', 'Mistral-7B']
resolved = [35, 24, 22, 19, 11, 3, 2, 1]
unresolved = [45, 56, 58, 61, 69, 77, 78, 79]
accuracy = [43.75, 30.00, 27.50, 23.75, 13.75, 3.75, 2.50, 1.25]

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']

fig, ax1 = plt.subplots(figsize=(11, 8), facecolor='#fafafa')
ax1.set_facecolor('#ffffff')

ax2 = ax1.twiny()

color_resolved = '#5ebd9d'   
color_unresolved = '#e07b7b'  
color_line = '#4a7bb7'       

y = np.arange(len(models))
height = 0.65

bars1 = ax1.barh(y, resolved, height, color=color_resolved, 
                 edgecolor='white', linewidth=2, zorder=3, label='Resolved Tasks')
bars2 = ax1.barh(y, unresolved, height, left=resolved, color=color_unresolved, 
                 edgecolor='white', linewidth=2, zorder=3, label='Unresolved Tasks')


for i in range(len(models)):
  
    if resolved[i] > 5:
        ax1.text(resolved[i]/2, i, str(resolved[i]),
                ha='center', va='center', fontsize=10, fontweight='bold',
                color='white', zorder=5)

    if unresolved[i] > 10:
        ax1.text(resolved[i] + unresolved[i]/2, i, str(unresolved[i]),
                ha='center', va='center', fontsize=10, fontweight='bold',
                color='white', zorder=5)


line = ax2.plot(accuracy, y, color=color_line, linewidth=3.5, 
                marker='o', markersize=9, markerfacecolor=color_line, 
                markeredgecolor='white', markeredgewidth=2.5,
                label='Accuracy', zorder=4, alpha=0.9)


for i, acc in enumerate(accuracy):
    ax2.text(acc + 3, i + 0.5, f'{acc}%',
            ha='left', va='center', fontsize=9, fontweight='600',
            color='#2a2a2a', 
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white', 
                     edgecolor='none', alpha=0.95),
            zorder=10)


ax1.set_xlabel('Number of Trials (out of 80)', fontsize=13, fontweight='600', 
               color='#4a4a4a', labelpad=10)
ax1.set_ylabel('Model', fontsize=13, fontweight='600', color='#4a4a4a', labelpad=10)
ax1.set_yticks(y)
ax1.set_yticklabels(models, fontsize=11, color='#5a5a5a')
ax1.set_xlim(0, 85)
ax1.set_xticks([0, 20, 40, 60, 80])
ax1.tick_params(axis='x', labelsize=10, colors='#6a6a6a')


ax1.invert_yaxis()


ax2.set_xlabel('Accuracy (%)', fontsize=13, fontweight='600', 
               color=color_line, labelpad=10)
ax2.set_xlim(0, 55)
ax2.set_xticks([0, 10, 20, 30, 40, 50])
ax2.tick_params(axis='x', labelsize=10, colors=color_line)
ax2.spines['top'].set_color(color_line)
ax2.spines['top'].set_linewidth(2)


ax1.grid(axis='x', alpha=0.15, linestyle='-', linewidth=0.8, color='#d0d0d0', zorder=0)
ax1.set_axisbelow(True)


ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_color('#dadada')
ax1.spines['bottom'].set_color('#dadada')


ax1.set_title('Terminal-Bench Performance: Task Completion & Accuracy Analysis', 
             fontsize=15, fontweight='700', color='#2a2a2a', pad=20)


from matplotlib.patches import Patch
from matplotlib.lines import Line2D
legend_elements = [
    Patch(facecolor=color_resolved, edgecolor='white', linewidth=2, label='Resolved Tasks'),
    Patch(facecolor=color_unresolved, edgecolor='white', linewidth=2, label='Unresolved Tasks'),
    Line2D([0], [0], color=color_line, linewidth=3.5, marker='o', markersize=9,
           markerfacecolor=color_line, markeredgecolor='white', markeredgewidth=2.5,
           label='Accuracy (%)')
]
ax1.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1.02, 0.5), 
          fontsize=11, frameon=True, fancybox=True, shadow=False, framealpha=0.95,
          edgecolor='#dadada')


fig.text(0.99, 0.01, 'Total: 80 tasks per model', 
         ha='right', va='bottom', fontsize=9, color='#9a9a9a', style='italic')

plt.tight_layout()
plt.savefig('terminal_bench_horizontal.png', dpi=300, bbox_inches='tight', facecolor='#fafafa')
plt.show()
