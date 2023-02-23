import pandas as pd

class CorrelationMatrix:
    def __init__(self, data):
        self.data = data
    
    def corr_matrix(self, keyword):
        # Select columns that contain the keyword
        keyword_cols = [col for col in self.data.columns if keyword in col]
        keyword_df = self.data[keyword_cols]

        # Calculate correlation matrix
        correlation_matrix = keyword_df.corr()
        corr_df = pd.DataFrame(correlation_matrix)

        mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
        corr_heatmap = sns.heatmap(corr_df, cmap="YlGnBu", annot=True, annot_kws={"size": 7, "color": "black"}, mask=mask)
        corr_heatmap.set_xticklabels(corr_heatmap.get_xticklabels(), fontsize=7)
        corr_heatmap.set_yticklabels(corr_heatmap.get_yticklabels(), fontsize=7)

        plt.show()  

corr = CorrelationMatrix(data)
corr_matrix = corr.corr_matrix('quantity')