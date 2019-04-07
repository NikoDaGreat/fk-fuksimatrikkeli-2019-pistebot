pelaajat=[1 2];
pisteet=pist([2 3 5 7 0; 2 6 1 67 4;]');
t=1:1:size(pelaajat);

%% PLOTIT %%
plot(t, pisteet, 'x', 'LineWidth', 4, 'Color', [93.3, 30.6, 47.5]./100)
axis([1 size(pelaajat) 0 max(pisteet)+5])
xlabel('Pelaaja')
ylabel('Pisteet')
title(datestr(now,31))