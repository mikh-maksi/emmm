

f1 = 2*x
f2 = 0.5*x
f3 = 24-x


# вказуємо в аргументі label текст легенди
plt.plot(x, f1, '--y', label='$x_2<2x_1$')
plt.plot(x, f2, '--b', label='$x_2>\\frac{1}{4}x_1$')
plt.plot(x, f3, '--g', label='$x_2<24-x_1$')




plt.scatter(7.9, 16.1, marker='s')
plt.scatter(15.9, 8, marker='s')
plt.scatter(0, 0, marker='^')


polygon_2 = matplotlib.patches.Polygon([(0, 0),
                                            (7.9, 16.1),
                                            (15.9, 8)],
                                           fill='blue',
                                           closed=True)

axes = plt.gca()
axes.set_aspect("equal")
axes.add_patch(polygon_2)


plt.arrow (x= 0 , y= 0 , dx=2 , dy= 4 , facecolor= 'red',edgecolor= 'none', width= .18 )
plt.annotate('Цільова функція', xy = (0.5, 0.5))

plt.xlabel(r'$x1$', fontsize=16)
plt.ylabel(r'$x2$', fontsize=16)

plt.xlim([0, 30])
plt.ylim([0, 30])

plt.legend(fontsize=14)
plt.grid()
plt.tight_layout()
plt.show()