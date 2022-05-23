# This program plots the views, ratings, and guest appearances of episodes of the Office.
#TODO Add legend
import pandas
import matplotlib.pyplot as plt
tv_data = pandas.read_csv("the_office_series.csv", index_col=0)

# print(list(tv_data.columns))
# ['Season', 'EpisodeTitle', 'About', 'Ratings', 'Votes', 'Viewership', 'Duration', 'Date', 'GuestStars', 'Director', 'Writers']

guest_stars = []
star_marker = []
# Create a pandas Series called has_stars that uses pandas.notna(elements)
# to return Boolean for if data is null
has_stars = pandas.notna(tv_data["GuestStars"])
no_stars = pandas.isna(tv_data["GuestStars"])
for ep_num, episode in has_stars.items():
    if episode == True:
        guest_stars.append(250)
        # star_marker.append("*")
    else:
        guest_stars.append(25)
        # star_marker.append("o")

tv_data["Size"] = guest_stars

colors = []
percentile_1 = tv_data["Ratings"].quantile(0.25)
percentile_2 = tv_data["Ratings"].quantile(0.5)
percentile_3 = tv_data["Ratings"].quantile(0.75)

for ep_num, episode in tv_data.iterrows():
    ratings = tv_data.loc[ep_num, "Ratings"]
    if ratings < percentile_1:
        colors.append("red")
    elif ratings < percentile_2:
        colors.append("orange")
    elif ratings < percentile_3:
        colors.append("lightgreen")
    else:
        colors.append("darkgreen")

tv_data["Colors"] = colors
print(tv_data)

max_view_index = tv_data["Viewership"].idxmax()
max_view = tv_data["Viewership"].max()
top_star = tv_data.loc[max_view_index, "GuestStars"]

plot_has_stars = tv_data[has_stars]
plot_no_stars = tv_data[no_stars]

plt.scatter(plot_has_stars.index, plot_has_stars["Viewership"], s=plot_has_stars["Size"], c=plot_has_stars["Colors"],
            marker="*", label=" Has guest stars")
plt.scatter(plot_no_stars.index, plot_no_stars["Viewership"], s=plot_no_stars["Size"], c=plot_no_stars["Colors"])
plt.title("Popularity, Quality, and Guest Appearances on the Office")
plt.xlabel("Episode Number")
plt.ylabel("Viewership (Millions)")
plt.text(max_view_index, max_view, top_star, size=8, horizontalalignment="center")

leg1 = plt.Line2D([], [], color="black", marker="*", ls="", label="Has guest stars")
leg2 = plt.Line2D([], [], color="darkgreen", marker=".", ls="", label="High rating")
leg3 = plt.Line2D([], [], color="lightgreen", marker=".", ls="", label="Med-high rating")
leg4 = plt.Line2D([], [], color="orange", marker=".", ls="", label="Med-low rating")
leg5 = plt.Line2D([], [], color="red", marker=".", ls="", label="Low rating")

# plt.legend(title="$\\bf{Legend}$", loc=7)
plt.legend(handles=[leg1, leg2, leg3, leg4, leg5], title="$\\bf{Legend}$")
plt.show()
