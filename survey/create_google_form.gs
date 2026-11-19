/**
 * Creates the "From Trend to Waste" consumer survey as a Google Form in YOUR Google account.
 *
 * How to run (about 2 minutes):
 *   1. Open https://script.google.com and click "New project".
 *   2. Delete the sample code, paste this whole file, then press Save (Ctrl/Cmd + S).
 *   3. In the toolbar, make sure the function "createSurveyForm" is selected and click Run.
 *   4. Google asks for permission to manage your forms: review and allow it (it is your own script).
 *   5. Open "Execution log" at the bottom: it prints the EDIT link (for you) and the SHARE link (for respondents).
 *
 * Do NOT rename questions: every title starts with a code (Q0., Q1., Q8a. ...) and
 * src/survey_analysis.py finds the columns of the exported CSV by these codes.
 * Mirrors survey/questionnaire.md and survey/conjoint_design.csv.
 */

var LIKERT_INFLUENCE = ['1 Not at all', '2', '3', '4', '5 Very much'];
var LIKERT_AGREE = ['1 Strongly disagree', '2', '3', '4', '5 Strongly agree'];
var FREQUENCY = ['Never', 'Rarely', 'Sometimes', 'Often', 'Always'];

// Conjoint profiles — must match survey/conjoint_design.csv (orthogonal 2^(4-1) design)
var PROFILES = [
  ['P1', 'Rs 799', 'Timeless', '1 season (about 20 wears)', 'No label'],
  ['P2', 'Rs 1,499', 'Timeless', '1 season (about 20 wears)', 'Certified sustainable'],
  ['P3', 'Rs 799', 'Trendy', '1 season (about 20 wears)', 'Certified sustainable'],
  ['P4', 'Rs 1,499', 'Trendy', '1 season (about 20 wears)', 'No label'],
  ['P5', 'Rs 799', 'Timeless', '3+ years (100+ wears)', 'Certified sustainable'],
  ['P6', 'Rs 1,499', 'Timeless', '3+ years (100+ wears)', 'No label'],
  ['P7', 'Rs 799', 'Trendy', '3+ years (100+ wears)', 'No label'],
  ['P8', 'Rs 1,499', 'Trendy', '3+ years (100+ wears)', 'Certified sustainable'],
];

function createSurveyForm() {
  var form = FormApp.create('Clothing Buying, Use and Disposal — Student Research Survey');
  form.setDescription(
    'This anonymous survey is part of a university Business Data Analytics project on clothing purchase and ' +
    'disposal. It takes about 10 minutes. We do not collect your name, email, phone number or any identifying ' +
    'information. Participation is voluntary and you can stop at any time by closing the form. Answers are ' +
    'reported only in aggregate for academic purposes.');
  form.setCollectEmail(false);
  form.setProgressBar(true);
  form.setAllowResponseEdits(false);
  form.setShowLinkToRespondAgain(false);
  form.setConfirmationMessage('Thank you! Your answers help us understand how clothing is bought, used and thrown away.');

  // ---- Section 0: consent (No -> submit immediately)
  var consent = form.addMultipleChoiceItem().setTitle('Q0. Do you agree to take part?').setRequired(true);
  form.addPageBreakItem().setTitle('Section 1 — About you');
  consent.setChoices([
    consent.createChoice('Yes, I agree', FormApp.PageNavigationType.CONTINUE),
    consent.createChoice('No (the form ends)', FormApp.PageNavigationType.SUBMIT),
  ]);

  // ---- Section 1: about you
  choice(form, 'Q1. Age group', ['Under 18', '18-24', '25-34', '35-44', '45-54', '55+']);
  choice(form, 'Q2. Occupation', ['Student', 'Working full-time', 'Working part-time / freelance', 'Homemaker',
                                  'Not working / retired', 'Prefer not to say']);
  choice(form, 'Q3. Where do you live?', ['Metro city', 'Other city / town', 'Village / rural area']);
  choice(form, 'Q4. Roughly how much do you spend on clothes in a typical month?',
         ['Less than Rs 1,000', 'Rs 1,000 - 2,999', 'Rs 3,000 - 4,999', 'Rs 5,000 or more']);

  // ---- Section 2: how you shop
  form.addPageBreakItem().setTitle('Section 2 — How you shop');
  choice(form, 'Q5. How often do you buy clothes?',
         ['Monthly or more', '5-11 times a year', '2-4 times a year', 'Once a year or less']);
  choice(form, 'Q6. Where do you buy clothes most often?',
         ['Mostly online', 'Mostly in stores', 'About equally online and in stores']);
  form.addCheckboxItem().setTitle('Q7. Which kinds of brands do you buy most?')
    .setHelpText('Select all that apply.')
    .setChoiceValues(['Fast-fashion brands (e.g. Zara, H&M, Shein-style, Max, Westside, Myntra/Ajio own labels)',
                      'Mid-price / premium brands', 'Local shops / unbranded', 'Second-hand / thrift', 'Other'])
    .setRequired(true);
  grid(form, 'Q8. How much does each reason influence your clothing purchases?', [
    'Q8a. It is in trend / fashionable right now',
    'Q8b. It is on discount / sale',
    'Q8c. It is new / I want something different',
    'Q8d. Quality and durability',
    'Q8e. Environmental / ethical reasons',
  ], LIKERT_INFLUENCE, '1 = Not at all, 5 = Very much');
  choice(form, 'Q9. In the last 3 months, how many clothing items did you buy that you had not planned to buy?',
         ['None', '1-2', '3-5', '6 or more']);

  // ---- Section 3: how you use clothes
  form.addPageBreakItem().setTitle('Section 3 — How you use clothes');
  choice(form, 'Q10. How many times do you typically wear a fast-fashion item before you stop wearing it?',
         ['Fewer than 5 times', '5-10 times', '11-30 times', '31-50 times', 'More than 50 times']);
  choice(form, 'Q11. How long do you typically keep a clothing item before you stop using it?',
         ['Less than 6 months', '6-12 months', '1-2 years', '2-3 years', 'More than 3 years']);
  choice(form, 'Q12. About what share of the clothes in your wardrobe did you NOT wear at all in the last 12 months?',
         ['Less than 10%', '10-25%', '26-50%', 'More than 50%']);

  // ---- Section 4: disposal
  form.addPageBreakItem().setTitle('Section 4 — What happens to clothes you no longer use');
  grid(form, 'Q13-Q18. How often do you do each of these with clothes you no longer use?', [
    'Q13. Sell / resell (online or offline)',
    'Q14. Donate to charity or people in need',
    'Q15. Hand down to family / friends',
    'Q16. Give for recycling / take-back schemes',
    'Q17. Throw away with household waste',
    'Q18. Keep them unused',
  ], FREQUENCY);

  // ---- Section 5: awareness and attitudes
  form.addPageBreakItem().setTitle('Section 5 — Awareness and attitudes');
  grid(form, 'Q19. How much do you agree?', [
    'Q19a. I know that making clothes uses a lot of water and energy',
    'Q19b. Fast fashion contributes to environmental damage',
    'Q19c. I would buy fewer clothes if they lasted longer',
    'Q19d. I would pay more for clothes that last longer',
    'Q19e. Brands should produce fewer items and sell more of what they make',
  ], LIKERT_AGREE, '1 = Strongly disagree, 5 = Strongly agree');
  form.addParagraphTextItem()
    .setTitle('Q20. (Optional) Anything else you want to say about how you buy or dispose of clothes?')
    .setRequired(false);

  // ---- Section 6: conjoint
  form.addPageBreakItem().setTitle('Section 6 — Which would you buy?').setHelpText(
    'Imagine you are buying a top/shirt. Each option below differs in price, style, how long it lasts, and ' +
    'whether it has a sustainability certificate. Rate how likely you are to buy each one.');
  for (var i = 0; i < PROFILES.length; i++) {
    var p = PROFILES[i];
    form.addScaleItem()
      .setTitle('Q' + (21 + i) + '. Option ' + p[0] + ' — ' + p[1] + ' · ' + p[2] + ' · Lasts ' + p[3] + ' · ' + p[4])
      .setBounds(1, 10)
      .setLabels('Definitely would not buy', 'Definitely would buy')
      .setRequired(true);
  }

  // ---- Publish and print links
  try { if (typeof form.setPublished === 'function') form.setPublished(true); } catch (e) { Logger.log('Publish it from the form editor: ' + e); }
  try { form.setAcceptingResponses(true); } catch (e) { Logger.log('Turn on "Accepting responses" in the Responses tab: ' + e); }
  Logger.log('EDIT the form (you):         ' + form.getEditUrl());
  Logger.log('SHARE with respondents:      ' + form.getPublishedUrl());
  try { Logger.log('Short share link:            ' + form.shortenFormUrl(form.getPublishedUrl())); } catch (e) {}
}

function choice(form, title, values) {
  return form.addMultipleChoiceItem().setTitle(title).setChoiceValues(values).setRequired(true);
}

function grid(form, title, rows, columns, help) {
  var g = form.addGridItem().setTitle(title).setRows(rows).setColumns(columns).setRequired(true);
  if (help) g.setHelpText(help);
  return g;
}
