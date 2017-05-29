Statistically speaking, what does baseline correction do?

To avoid confusion, let's first state what baseline correction is *not*. Baseline correction is *not* a way to control for overall differences in pupil size between participants. Of course, some participants have larger pupils than others [see @Tsukahara2016 for a fascinating study on the relationship between pupil size and intelligence]; and the distance between camera and eye, which varies slightly from participant to participant, also affects pupil size, at least as measured by most eye trackers. But such between-subject differences are better taken into account statistically, through a repeated measures ANOVA or a linear mixed-effects model with by-participant random intercepts [e.g. @Baayen2008JMemLang]—just like between-subject differences in reaction times are usually taken into account.

Instead, baseline correction is a way to reduce the impact of random pupil-size fluctuations from one trial to the next. In an analysis *without* baseline correction, pupil sizes are compared between trials; for example, all trials in one condition are compared to all trials in another condition. You can think of this as a between-trial analysis. In such a between-trial analysis, random fluctuations in pupil size from one trial to the next are a source of noise, and decrease statistical power for detecting true differences between conditions.

In contrast, in an analysis *with* baseline correction, pupil sizes are first compared between the baseline epoch and another moment in the same trial. The dependent variable then becomes pupil-size change relative to baseline; pupil-size change is first determined for each trial, and then further compared between trials. You can think of this as a within-trial analysis, that is, an analysis in which Trial is taken into account as a random effect (i.e. a factor with a non-systematic effect). In a within-trial analysis, slow and random fluctuations in pupil size from one trial to the next are no longer a source of source, and no longer decrease statistical power. This is why baseline correction improves statistical power.

The observation that baseline correction is similar to treating Trial as a random effect deserves further consideration. Because subtractive baseline correction is not merely similar to treating Trial as a random effect—it is in every way identical. To illustrate this, let's consider two ways to analyze pupil-size data, as shown in %FigStatistics. These two ways seem very different at first sight, but are equivalent on closer inspection.

Here, we have hypothetical data of four trials with two conditions (Blue and Red). Let's assume that we want to analyze the effect of condition at time 1. (The exact same principles would apply if we wanted to analyze the effect of condition at time 2.)


%--
figure:
 id: FigStatistics
 source: FigStatistics.svg
 caption: |
  Two different ways to take baseline pupil size into account. a) Baseline pupil size can be taken into account statistically, by conducting a linear mixed-effects model. b) After performing subtractive baseline correction, the same analysis is reduced to independent-samples t-test. 
--%


%FigStatistics::a shows an analysis that takes baseline pupil size into account by treating Trial as a random effect, without doing explicit baseline correction. To do so, the analysis includes two time points for each trial: one time point (0) that corresponds to the baseline, and one time point (1) that corresponds to the sample that we want to analyze. We are then interested in the interaction between time and condition: This reflects the effect of condition, while taking changes in baseline pupil size into account. Because each trial now contributes two observations to the analysis, the observations in the analysis are no longer independent. To take this into account, we need to conduct a linear mixed-effects model where Trial is a random effect, and we allow the intercept to randomly vary by Trial (i.e. random by-Trial intercepts). The outcome of this analysis is t = 2.668, p = 0.116 for the time × condition interaction.

%FigStatistics::b shows the same analysis, but done after subtractive baseline correction, so that pupil size is set to 0 at time 0 for all trials. The analysis now reduced to a simple independent samples t-test between the Blue and Red trials. The outcome is t = 2.668, p = 0.116—identical to the linear-mixed effects analysis described above.

In other words, by treating Trial as a random effect in an analysis, you can accomplish the exact same thing as by doing subtractive baseline correction. However, in most cases baseline correction is simpler to do. Specifically, it avoids the need for complex statistical models with multiple random effects (generally at least two: Trial and Participant). This is especially relevant for researchers who prefer to analyze their data with a repeated measures ANOVA, which allows for only a single random effect, and that role is generally already reserved for Participant.
