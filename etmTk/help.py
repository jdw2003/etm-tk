OVERVIEW = """\
In contrast to most calendar/todo applications, creating
items (events, tasks, and so forth) in etm does not require
filling out fields in a form. Instead, items are created as
free-form text entries using a simple, intuitive format and
stored in plain text files.

Items in etm begin with a type character such as an asterisk
(event) and continue on one or more lines either until the
end of the file is reached or another line is found that
begins with a type character. The beginning type character
for each item is followed by the item summary and then,
perhaps, by one or more @key value pairs. The order in which
such pairs are entered does not matter.

Sample entries

-   A sales meeting (an event) [s]tarting seven days from
    today at 9:00am and [e]xtending for one hour with a
    default [a]lert 5 minutes before the start:

        * sales meeting @s +7 9a @e 1h @a 5

-   The sales meeting with another [a]lert 2 days before the
    meeting to (e)mail a reminder to a list of recipients:

        * sales meeting @s +7 9a @e 1h @a 5
          @a 2d: e; who@when.com, what@where.org

-   Prepare a report (a task) for the sales meeting
    [b]eginning 3 days early:

        - prepare report @s +7 @b 3

-   A period [e]xtending 35 minutes (an action) spent
    working on the report yesterday:

        ~ report preparation @s -1 @e 35

-   Get a haircut (a task) on the 24th of the current month
    and then [r]epeatedly at (d)aily [i]ntervals of (14)
    days and, [o]n completion, (r)estart from the completion
    date:

        - get haircut @s 24 @r d &i 14 @o r

-   Payday (an occassion) on the last week day of each
    month. The &s -1 part of the entry extracts the last
    date which is both a weekday and falls within the last
    three days of the month):

        ^ payday @s 1/1 @r m &w (MO, TU, WE, TH, FR)
          &m (-1, -2, -3) &s -1

-   Take a prescribed medication daily (a reminder)
    [s]tarting today and [r]epeating (d)aily at [h]ours
    10am, 2pm, 6pm and 10pm [u]ntil (12am on) the fourth day
    from today. Trigger the default [a]lert zero minutes
    before each event:

        * take Rx @s +0 @r d &h 10, 14, 18, 22 &u +4 @a 0

-   Presidential election day (an occasion) every four years
    on the first Tuesday after a Monday in November:

        ^ Presidential Election Day @s 2012-11-06
          @r y &i 4 &M 11 &m (2,3,4,5,6,7,8) &w TU

-   Join the etm discussion group (a task) [s]tarting on the
    first day of the next month. Because of the @g (goto)
    link, pressing Ctrl-G when the details of this item are
    displayed in the gui would open the link using the
    system default application which, in this case, would be
    your default browser:

        - join the etm discussion group @s +1/1
          @g http://groups.google.com/group/eventandtaskmanager/topics
"""

ITEMTYPES = """\
~ Action

A record of an action involving the expenditure of time (@e) and/or
money (@x). Actions are not reminders, they are instead records of how
time and/or money was actually spent. Action lines begin with a tilde,
~.

        ~ picked up lumber and paint @s mon 3p @e 1h15m @x 127.32

Entries such as @s mon 3p, @e 1h15m and @x 127.32 are discussed below
under Item details. Action entries form the basis for time and expense
billing using action reports - see help/reports.

* Event

Something that will happen on particular day(s) and time(s). Event lines
begin with an asterick, *.

        * dinner with Karen and Al @s sat 7p @e 3h

Events have a starting datetime, @s and an extent, @e. The ending
datetime is given implicitly as the sum of the starting datetime and the
extent. Events that span more than one day are possible, e.g.,

        * Sales conference @s 9a wed @e 2d8h

begins at 9am on Wednesday and ends at 5pm on Friday.

An event without an @e entry or with @e 0 is regarded as a reminder and,
since there is no extent, will not be displayed in the week view.

^ Occasion

Holidays, anniversaries, birthdays and the like. Like an event with a
date but no starting time and no extent. Occasions begin with a caret
sign, ^.

        ^ The !1776! Independence Day @s 2010-07-04 @r y &M 7 &m 4

On July 4, 2013, this would appear as The 237th Independence Day.

! Note

A record of some useful information. Note lines begin with an
exclamation point, !.

    ! xyz software @d user: dnlg, pw: abc123def

- Task

Something that needs to be done. It may or may not have a due date. Task
lines begin with a minus sign, -.

    - pay bills @s Oct 25

A task with an @s entry becomes due on that date and past due when that
date has passed. If the task also has an @b begin-by entry, then advance
warnings of the task will begin appearing the specified number of days
before the task is due. An @e entry in a task is interpreted as an
estimate of the time required to finish the task.

% Delegated task

A task that is assigned to someone else, usually the person designated
in an @u entry. Delegated tasks begin with a percent sign, %.

        % make reservations for trip @u joe @s fri

+ Task group

A collection of related tasks, some of which may be prerequities for
others. Task groups begin with a plus sign, +.

        + dog house
          @j pickup lumber and paint      &q 1
          @j cut pieces                   &q 2
          @j assemble                     &q 3
          @j paint                        &q 4

Note that a task group is a single item and is treated as such. E.g., if
any job is selected for editing then the entire group is displayed.

Individual jobs are given by the @j entries. The queue entries, &q, set
the order --- tasks with smaller &q values are prerequisites for
subsequent tasks with larger &q values. In the example above, neither
"pickup lumber" nor "pickup paint" have any prerequisites. "Pickup
lumber", however, is a prerequisite for "cut pieces" which, in turn, is
a prerequisite for "assemble". Both "assemble" and "pickup paint" are
prerequisites for "paint".

$ In basket

A quick, don't worry about the details item to be edited later when you
have the time. In basket entries begin with a dollar sign, $.

        $ joe 919 123-4567

If you create an item using etm and forget to provide a type character,
an $ will automatically be inserted.

? Someday maybe

Something are you don't want to forget about altogether but don't want
to appear on your next or scheduled lists. Someday maybe items begin
with a question mark, ?.

        ? lose weight and exercise more

# Hidden

Hidden items begin with a hash mark, #. Such items are ignored by etm
save for appearing in the folder view. Stick a hash mark in front of any
item that you don't want to delete but don't want to see in your other
views.

= Defaults

Default entries begin with an equal sign, =. These entries consist of
@key value pairs which then become the defaults for subsequent entries
in the same file until another = entry is reached.

Suppose, for example, that a particular file contains items relating to
"project_a" for "client_1". Then entering

    = @k client_1:project_a

on the first line of the file and

    =

on the twentieth line of the file would set the default keyword for
entries between the first and twentieth line in the file."""

DATES = """\
Fuzzy dates and time periods

When either a datetime or an time period is to be entered, special
formats are used in etm. Examples include entering a starting datetime
for an item using @s, jumping to a date using Ctrl-J and calculating a
date using F5.

Suppose, for example, that it is currently 8:30am on Friday, February
15, 2013. Then, fuzzy dates would expand into the values illustrated
below.

-   mon 2p or mon 14h: 2:00pm Monday, February 19
-   fri: 12:00am Friday, February 15
-   9a -1/1 or 9h -1/1: 9:00am Tuesday, January 1
-   +2/15: 12:00am Monday, April 15 2013
-   8p +7 or 20h +7: 8:00pm Friday, February 22
-   -14: 12:00am Friday, February 1
-   now: 8:30am Friday, February 15

Note that 12am is the default time when a time is not explicity entered.
E.g., +2/15 in the examples above gives 12:00am on April 15.

To avoid ambiguity, always append either 'a', 'p' or 'h' when entering
an hourly time, e.g., use 1p or 13h.

Time periods are entered using the format DdHhMm where D, H and M are
integers and d, h and m refer to days, hours and minutes respectively.
For example:

-   2h30m: 2 hours, 30 minutes
-   7d: 7 days
-   45m: 45 minutes

As an example, if it is currently 8:50am on Friday February 15, 2013,
then entering now + 2d4h30m into the date calculator would give
2013-02-17 1:20pm. If, at the same time, an item were saved on a system
in the US/Eastern time zone which contained the entry
@s now @z Australia/Sydney then the expanded value would be
@s 2013-02-16 12:50am, which is "now" in Sydney.

Dates and times are always stored in etm data files as times in the time
zone given by the entry for @z. On the other hand, dates and times are
always displayed in etm using the local time zone of the system. In the
previous illustration, for example, the data file would contain
@s 2013-02-16 12:50am @z Australia/Sydney but this item would be
displayed as starting at 2013-02-15 8:50am on a system in the US/Eastern
time zone.

Anniversary substitutions

An anniversary substitution is an expression of the form !YYYY! that
appears in an item summary. Consider, for example, the occassion

    ^ !2010! anniversary @s 2011-02-20 @r y

This would appear on Feb 20 of 2011, 2012, 2013 and 2014, respectively,
as 1st anniversary, 2nd anniversary, 3rd anniversary and 4th
anniversary.The suffixes, st, nd and so forth, depend upon the
translation file for the locale."""

ATKEYS = """\
@a alert

The specification of the alert(s) to use with the item. One or more
alerts can be specified in an item. E.g.,

    @a 10m, 5m
    @a 1h: s

would trigger the alert(s) specified by default_alert in your etm.cfg at
10 and 5 minutes before the starting time and a (s)ound alert one hour
before the starting time.

The alert

    @a 2d: e; who@what.com, where2@when.org; filepath1, filepath2

would send an email to the two listed recipients exactly 2 days (48
hours) before the starting time of the item with the item summary as the
subject, with file1 and file2 as attachments and with the body of the
message composed using email_template from your etm.cfg.

Similarly, the alert

    @a 10m: t; 9191234567@vtext.com, 9197654321@txt.att.net

would send a text message 10 minutes before the starting time of the
item to the two mobile phones listed (using 10 digit area code and
carrier mms extension) together with the settings for sms in etm.cfg. If
no numbers are given, the number and mms extension specified in
sms.phone will be used. Here are the mms extensions for the major US
carriers:

    Alltel          @message.alltel.com
    AT&T            @txt.att.net
    Nextel          @messaging.nextel.com
    Sprint          @messaging.sprintpcs.com
    SunCom          @tms.suncom.com
    T-mobile        @tmomail.net
    VoiceStream     @voicestream.net
    Verizon         @vtext.com

Finally,

    @a 0: p; program_path

would execute program_path at the starting time of the item.

The format for each of these:

    @a <trigger times> [: action [; arguments]]

In addition to the default action used when the optional : action is not
given, there are the following possible values for action:

-   d Execute alert_displaycmd in etm.cfg.
-   e; recipients[;attachments] Send an email to recipients (a comma
    separated list of email addresses) optionally attaching attachments
    (a comma separated list of file paths). The item summary is used as
    the subject of the email and the expanded value of email_template
    from etm.cfg as the body.
-   m Display an internal etm message box using alert_template.
-   p; process Execute the command given by process.
-   s Execute alert_soundcmd in etm.cfg.
-   t [; phonenumbers] Send text messages to phonenumbers (a comma
    separated list of 10 digit phone numbers with the sms extension of
    the carrier appended) with the expanded value of sms.message as the
    text message.
-   v Execute alert_voicecmd in etm.cfg.

Note: either e or p can be combined with other actions in a single alert
but not with one another.

@b beginby

An integer number of days before the starting date time at which to
begin displaying begin by notices. When notices are displayed they will
be sorted by the item's starting datetime and then by the item's
priority, if any.

@c context

Intended primarily for tasks to indicate the context in which the task
can be completed. Common contexts include home, office, phone, computer
and errands. The "next view" supports this usage by showing undated
tasks, grouped by context. If you're about to run errands, for example,
you can open the "next view", look under "errands" and be sure that you
will have no "wish I had remembered" regrets.

@d description

An elaboration of the details of the item to complement the summary.

@e extent

A time period string such as 1d2h (1 day 2 hours). For an action, this
would be the elapsed time. For a task, this could be an estimate of the
time required for completion. For an event, this would be the duration.
The ending time of the event would be this much later than the starting
datetime.

@f done[; due]

Datetimes; tasks, delegated tasks and task groups only. When a task is
completed an @f done entry is added to the task. When the task has a due
date, ; due is appended to the entry. Similarly, when a job from a task
group is completed in etm, an &f done or &f done; due entry is appended
to the job and it is removed from the list of prerequisites for the
other jobs. In both cases done is the completion datetime and due, if
added, is the datetime that the task or job was due. The completed task
or job is shown as finished on the completion date. When the last job in
a task group is finished an @f done or @f done; due entry is added to
the task group itself reflecting the datetime that the last job was done
and, if the task group is repeating, the &f entries are removed from the
individual jobs.

Another step is taken for repeating task groups. When the first job in a
task group is completed, the @s entry is updated using the setting for
@o (above) to show the next datetime the task group is due and the @f
entry is removed from the task group. This means when some, but not all
of the jobs for the current repetition have been completed, only these
job completions will be displayed. Otherwise, when none of the jobs for
the current repetition have been completed, then only that last
completion of the task group itself will be displayed.

Consider, for example, the following repeating task group which repeats
monthly on the last weekday on or before the 25th.

    + pay bills @s 11/23 @f 10/24;10/25
      @r m &w MO,TU,WE,TH,FR &m 23,24,25 &s -1
      @j organize bills &q 1
      @j pay on-line bills &q 3
      @j get stamps, envelopes, checkbook &q 1
      @j write checks &q 2
      @j mail checks &q 3

Here "organize bills" and "get stamps, envelopes, checkbook" have no
prerequisites. "Organize bills", however, is a prerequisite for "pay
on-line bills" and both "organize bills" and "get stamps, envelops,
checkbook" are prerequisites for "write checks" which, in turn, is a
prerequisite for "mail checks".

The repetition that was due on 10/25 was completed on 10/24. The next
repetition was due on 11/23 and, since none of the jobs for this
repetition have been completed, the completion of the group on 10/24 and
the list of jobs due on 11/23 will be displayed initially. The following
sequence of screen shots show the effect of completing the jobs for the
11/23 repetition one by one on 11/27.

@g goto

The path to a file or a URL to be opened using the system default
application when the user presses Control-G in the GUI.

@j job

Component tasks or jobs within a task group are given by @j job entries.
@key value entries prior to the first @j become the defaults for the
jobs that follow. &key value entries given in jobs use & rather than @
and apply only to the specific job.

Many key-value pairs can be given either in the group task using @ or in
the component jobs using &:

-   @c or &c: context
-   @d or &d: description
-   @e or &e: extent
-   @f or &f: done[; due] (datetimes)
-   @k or &k: keyword
-   @l or &l: location

The key-value pair &q (queue position) can only be given in component
jobs where it is required. Key-values other than &q and those listed
above, can only be given in the initial group task entry and their
values are inherited by the component jobs.

@k keyword

A heirarchical classifier for the item. Intended for actions to support
time billing where a common format would be client:job:category. etm
treats such a keyword as a heirarchy so that an action report grouped by
month and then keyword might appear as follows

        27.5h) Client 1 (3)
            4.9h) Project A (1)
            15h) Project B (1)
            7.6h) Project C (1)
        24.2h) Client 2 (3)
            3.1h) Project D (1)
            21.1h) Project E (2)
                5.1h) Category a (1)
                16h) Category b (1)
        4.2h) Client 3 (1)
        8.7h) Client 4 (2)
            2.1h) Project F (1)
            6.6h) Project G (1)

An arbitrary number of heirarchical levels in keywords is supported.

@l location

The location at which, for example, an event will take place.

@m memo

Further information about the item not included in the summary or the
description. Since the summary is used as the subject of an email alert
and the descripton is commonly included in the body of an email alert,
this field could be used for information not to be included in the
email.

@o overdue

Repeating tasks only. One of the following choices: k) keep, r) restart,
or s) skip. Details below.

@p priority

Either 0 (no priority) or an intger between 1 (highest priority) and 9
(lowest priority). Primarily used with undated tasks.

@r repetition rule

The specification of how an item is to repeat. Repeating items must have
an @s entry as well as one or more @r entries. Generated datetimes are
those satisfying any of the @r entries and falling on or after the
datetime given in @s. Note that the datetime given in @s will only be
included if it matches one of the datetimes generated by the @r entry.

A repetition rule begins with

    @r frequency

where frequency is one of the following characters:

-   y: yearly
-   m: monthly
-   m: weekly
-   d: daily
-   l: list (a list of datetimes will be provided using @+)

The @r frequency entry can, optionally, be followed by one or more
&key value pairs:

-   &i: interval (positive integer, default = 1) E.g, with frequency w,
    interval 3 would repeat every three weeks.
-   &t: total (positive integer) Include no more than this total number
    of repetitions.
-   &s: bysetpos (integer) See the payday example below for an
    illustration of bysetpos.
-   &u: until (datetime) Only include repetitions falling before (not
    including) this datetime.
-   &M: bymonth (1, 2, ..., 12)
-   &m: bymonthday (1, 2, ..., 31) Use, e.g., -1 for the last day of the
    month.
-   &W: byweekno (1, 2, ..., 53)
-   &w: byweekday (English weekday abbreviation SU ... SA). Use, e.g.,
    3WE for the 3rd Wednesday or -1FR, for the last Friday in the month.
-   &h: byhour (0 ... 23)
-   &n: byminute (0 ... 59)

Repetition examples:

-   1st and 3rd Wednesdays of each month.

        ^ 1st and 3rd Wednesdays
          @r m &w 1WE, 3WE

-   Payday (an occasion) on the last week day of each month. (The &s -1
    entry extracts the last date which is both a weekday and falls
    within the last three days of the month.)

        ^ payday @s 2010-07-01
          @r m &w MO, TU, WE, TH, FR &m -1, -2, -3 &s -1

-   Take a prescribed medication daily (an event) from the 23rd through
    the 27th of the current month at 10am, 2pm, 6pm and 10pm and trigger
    an alert zero minutes before each event.

        * take Rx @d 10a 23  @r d &u 11p 27 &h 10, 14 18, 22 @a 0

-   Vote for president (an occasion) every four years on the first
    Tuesday after a Monday in November. (The &m range(2,9) requires the
    month day to fall within 2 ... 8 and thus, combined with &w TU to be
    the first Tuesday following a Monday.)

        ^ Vote for president @s 2012-11-06
          @r y &i 4 &M 11 &m range(2,9) &w TU

Optionally, @+ and @- entries can be given.

-   @+: include (comma separated list to datetimes to be added to those
    generated by the @r entries)
-   @-: exclude (comma separated list to datetimes to be removed from
    those generated by the @r entries)

A repeating task may optionally also include an @o <k|s|r> entry
(default = k):

-   @o k: Keep the current due date if it becomes overdue and use the
    next due date from the recurrence rule if it is finished early. This
    would be appropriate, for example, for the task 'file tax return'.
    The return due April 15, 2009 must still be filed even if it is
    overdue and the 2010 return won't be due until April 15, 2010 even
    if the 2009 return is finished early.

-   @o s: Skip overdue due dates and set the due date for the next
    repetition to the first due date from the recurrence rule on or
    after the current date. This would be appropriate, for example, for
    the task 'put out the trash' since there is no point in putting it
    out on Tuesday if it's picked up on Mondays. You might just as well
    wait until the next Monday to put it out. There's also no point in
    being reminded until the next Monday.

-   @o r: Restart the repetitions based on the last completion date.
    Suppose you want to mow the grass once every ten days and that when
    you mowed yesterday, you were already nine days past due. Then you
    want the next due date to be ten days from yesterday and not today.
    Similarly, if you were one day early when you mowed yesterday, then
    you would want the next due date to be ten days from yesterday and
    not ten days from today.

@s starting datetime

When an action is started, an event begins or a task is due.

@t tags

A tag or list of tags for the item.

@u user

Intended to specify the person to whom a delegated task is assigned.
Could also be used in actions to indicate the person performing the
action.

@v action_rates key

Actions only. A key from action_rates in your etm.cft to apply to the
value of @e. Used in actions to apply a billing rate to time spent in an
action. E.g., with

        minutes: 6
        action_rates:
            br1: 45.0
            br2: 60.0

then entries of @v br1 and @e 2h25m in an action would entail a value of
45.0 * 2.5 = 112.50.

@w action_markups key

A key from action_markups in your etm.cfg to apply to the value of @x.
Used in actions to apply a markup rate to expense in an action. E.g.,
with

        weights:
            mr1: 1.5
            mr2: 10.0

then entries of @w mr1 and @x 27.50 in an action would entail a value of
27.50 * 1.5 = 41.25.

@x expense

Actions only. A currency amount such as 27.50. Used in conjunction with
@w above to bill for action expenditures.

@z time zone

The time zone of the item, e.g., US/Eastern. The starting and other
datetimes in the item will be interpreted as belonging to this time
zone.

@+ include

A datetime or list of datetimes to be added to the repetitions generated
by the @r rrule entry. If only a date is provided, 12:00am is assumed.

@- exclude

A datetime or list of datetimes to be removed from the repetitions
generated by the @r rrule entry. If only a date is provided, 12:00am is
assumed.

Note that to exclude a datetime from the recurrence rule, the @-
datetime must exactly match both the date and time generated by the
recurrence rule."""

PREFERENCES = """\
Each configuration option is listed below with an illustrative entry and
a brief discussion. These entries are stored, by default, in
~/.etm/etm.cfg. When this file is edited in etm (Shift Ctrl-O), your
changes become effective as soon as they are saved --- you do not need
to restart etm.

The following template expansions can be used in alert_displaycmd,
alert_template, alert_voicecmd, email_template, sms_message and
sms_subject below.

-   !summary!: the item's summary (this will be used as the subject of
    email and message alerts)
-   !start_date!: the starting date of the event
-   !start_time!: the starting time of the event
-   !time_span!: the time span of the event (see below)
-   !alert_time!: the time the alert is triggered
-   !time_left!: the time remaining until the event starts
-   !when!: the time remaining until the event starts as a sentence (see
    below)
-   !d!: the item's @d (description)
-   !l!: the item's @l (location)

The value of !time_span! depends on the starting and ending datetimes.
Here are some examples:

-   if the start and end datetimes are the same (zero extent):
    10am Wed, Aug 4

-   else if the times are different but the dates are the same:
    10am - 2pm Wed, Aug 4

-   else if the dates are different: 10am Wed, Aug 4 - 9am Thu, Aug 5

-   additionally, the year is appended if a date falls outside the
    current year:

        10am - 2pm Thu, Jan 3 2013
        10am Mon, Dec 31 - 2pm Thu, Jan 3 2013

Here are values of !time_left! and !when! for some illustrative periods:

-   2d3h15m

        time_left : '2 days 3 hours 15 minutes'
        when      : '2 days 3 hours 15 minutes from now'

-   20m

        time_left : '20 minutes'
        when      : '20 minutes from now'

-   0m

        time_left : ''
        when      : 'now'

Note that 'now', 'from now', 'days', 'day', 'hours' and so forth are
determined by the translation file in use.

Available template expansions for action_template (below) include:

-   !label! the item or group label.
-   !count! the number of children represented in the reported item or
    group.
-   !minutes! the total time from @e entries in minutes rounded up using
    the setting for action_minutes.
-   !hours! if action_minutes = 1, the time in hours and minutes.
    Otherwise, the time in floating point hours.
-   !value! the billing value of the rounded total time. Requires an
    action entry such as @v br1 and a setting for action_rates.
-   !expense! the total expense from @x entries.
-   !charge! the billing value of the total expense. Requires an action
    entry such as @w mu1 and a setting for action_markups.
-   !total! the sum of !value! and !charge!.

Note: when aggregating amounts in action reports, billing and markup
rates are applied first to times and expenses for individual actions and
the resulting amounts are then aggregated. Similarly, when times are
rounded up, the rounding is done for individual actions and the results
are then aggregated.

action_interval

    action_interval: 1

Every action_interval minutes, execute action_timercmd when the timer is
running and action_pausecmd when the timer is paused. Choose zero to
disable executing these commands.

action_markups

    action_markups:
        default: 1.0
        mu1: 1.5
        mu2: 2.0

Possible markup rates to use for @x expenses in actions. An arbitrary
number of rates can be entered using whatever labels you like. These
labels can then be used in actions in the @w field so that, e.g.,

    ... @x 25.80 @w mu1 ...

in an action would give this expansion in an action template:

    !expense! = 25.80
    !charge! = 38.70

action_minutes

    action_minutes: 6

Round action times up to the nearest action_minutes in action reports.
Possible choices are 1, 6, 12, 15, 30 and 60. With 1, no rounding is
done and times are reported as integer minutes. Otherwise, the
prescribed rounding is done and times are reported as floating point
hours.

action_rates

    <!-- action_rates: -->
        default: 30.0
        br1: 45.0
        br2: 60.0

Possible billing rates to use for @e times in actions. An arbitrary
number of rates can be entered using whatever labels you like. These
labels can then be used in the @v field in actions so that, e.g., with
action_minutes: 6 then:

    ... @e 75m @v br1 ...

in an action would give these expansions in an action template:

    !hours! = 1.3
    !value! = 58.50

If the label default is used, the corresponding rate will be used when
@v is not specified in an action.

Note that etm accumulates group totals from the time and value of
individual actions. Thus

    ... @e 75m @v br1 ...
    ... @e 60m @v br2 ...

would aggregate to

    !hours!  = 2.3     (= 1.3 + 1)
    !value! = 118.50   (= 1.3 * 45.0 + 1 * 60.0)

action_template

    action_template: '!hours!h) !label! (!count!)'

Used for action reports. With the above settings for action_minutes and
action_template, a report might appear as follows:

    27.5h) Client 1 (3)
        4.9h) Project A (1)
        15h) Project B (1)
        7.6h) Project C (1)
    24.2h) Client 2 (3)
        3.1h) Project D (1)
        21.1h) Project E (2)
            5.1h) Category a (1)
            16h) Category b (1)
    4.2h) Client 3 (1)
    8.7h) Client 4 (2)
        2.1h) Project F (1)
        6.6h) Project G (1)

action_timer

    action_timer:
        paused: '/usr/bin/play /home/dag/.etm/sounds/timer_paused.wav'
        running: '/usr/bin/play /home/dag/.etm/sounds/timer_running.wav'

The command running is executed every action_interval minutes whenever
the action timer is running and paused every minute when the action
timer is paused.

action_status

    action_status:
        paused:    'echo !summary! !time! paused > ~/.etm/status.text'
        running:   'echo !summary! !time! running > ~/.etm/status.text'
        stopped:   'echo  > ~/.etm/status.text'

The expansion of the appropriate command will be executed whenever the
status of the action timer changes.

Available expansions for paused, running and stopped include:

-   !summary! the action summary.
-   !time! the current value of timer in H:MM format.

The illustrative running might, for example, expand as follows:

    jones deposition 0:27 running

With the above example, note that an application such as conky or
geektool could be used to display the contents of ~/.etm/status.text on
the user's desktop.

agenda

    agenda_colors:  2
    agenda_days:    4
    agenda_indent:  2
    agenda_width1: 24
    agenda_width2:  8

The agenda setup. With colors 2, all colors are used, with 1 only red is
used (past due tasks) and with 0 no colors are used. days is the number
of active days to display. indent gives the indentation for each level
of the tree. width1 and width2 give, respectively, the maximum width for
columns 1 and 2.

alert_default

    alert_default: [m]

The alert or list of alerts to be used when an alert is specified for an
item but the type is not given. Possible values for the list include: -
d: display (requires alert_displaycmd) - m: message (using
alert_template) - s: sound (requires alert_soundcmd) - v: voice
(requires alert_voicecmd)

alert_displaycmd

    alert_displaycmd: /usr/local/bin/growlnotify -t !summary! -m '!time_span!'

The command to be executed when d is included in an alert. Possible
template expansions are discussed at the beginning of this tab.

alert_soundcmd

    alert_soundcmd: '/usr/bin/play /home/dag/.etm/sounds/etm_alert.wav'

The command to execute when s is included in an alert. Possible template
expansions are discussed at the beginning of this tab.

alert_template

    alert_template: '!time_span!\n!l!\n\n!d!'

The template to use for the body of m (message) alerts. See the
discussion of template expansions at the beginning of this tab for other
possible expansion items.

alert_voicecmd

    alert_voicecmd: /usr/bin/say -v 'Alex' '!summary! begins !when!.'

The command to be executed when v is included in an alert. Possible
expansions are are discussed at the beginning of this tab.

alert_wakecmd

    alert_wakecmd: /Users/dag/bin/SleepDisplay -w

If given, this command will be issued to "wake up the display" before
executing alert_displaycmd.

ampm

    ampm: true

Use ampm times if true and twenty-four hour times if false. E.g., 2:30pm
(true) or 14:30 (false).

auto_completions

        auto_completions: ~/.etm/completions.cfg

The absolute path to the file to be used for autocompletions. Each line
in the file provides a possible completion. E.g.

    @c computer
    @c home
    @c errands
    @c office
    @c phone
    @z US/Eastern
    @z US/Central
    @z US/Mountain
    @z US/Pacific
    dnlgrhm@gmail.com

As soon as you enter, for example, "@c" in the editor, a list of
possible completions will pop up and then, as you type further
characters, the list will shrink to show only those that still match:

[]
Up and down arrow keys change the selection and either Tab or Return
inserts the selection.

calendars

    calendars:
    - [dag, true, personal/dag]
    - [erp, false, personal/erp]
    - [shared, true, shared]

These are (label, default, path relative to datadir) tuples to be
interpreted as separate calendars. Those for which default is true will
be displayed as default calendars. E.g., with the datadir below, dag
would be a default calendar and would correspond to the absolute path
/Users/dag/.etm/data/personal/dag. With this setting, the calendar
selection dialog would appear as follows:

[]
When non-default calendars are selected, busy times in the "week view"
will appear in one color for events from default calendars and in
another color for events from non-default calendars.

Note that the calendar icon only appears in the main gui if this setting
is provided.

current files

    current_htmlfile:  ''
    current_textfile:  ''
    current_indent:    3
    current_opts:      ''
    current_width1:    40
    current_width2:    17

If absolute file paths are entered for current_textfile and/or
current_htmlfile, then these files will be created and automatically
updated by etm as as plain text or html files, respectively. If
current_opts is given then the file will contain a report using these
options; otherwise the file will contain an agenda. Indent and widths
are taken from these setting with other settings, including color, from
report or agenda, respectively.

Hint: fans of geektool can use the shell command cat <current_textfile>
to have the current agenda displayed on their desktops.

datadir

    datadir: ~/.etm/data

All etm data files are in this directory.

dayfirst

    dayfirst: false

If dayfirst is False, the MM-DD-YYYY format will have precedence over
DD-MM-YYYY in an ambiguous date. See also yearfirst.

edit_cmd

    edit_cmd: ~/bin/vim !file! +!line!

This command is used in the command line version of etm to create and
edit items. When the command is expanded, !file! will be replaced with
the complete path of the file to be edited and !line! with the starting
line number in the file. If the editor will open a new window, be sure
to include the command to wait for the file to be closed before
returning, e.g., with vim:

    edit_cmd: ~/bin/gvim -f !file! +!line!

or with sublime text:

    edit_cmd: ~/bin/subl -n -w !file!:!line!

email_template

    email_template: 'Time: !time_span!
    Locaton: !l!


    !d!'

Note that two newlines are required to get one empty line when the
template is expanded. This template might expand as follows:

        Time: 1pm - 2:30pm Wed, Aug 4
        Location: Conference Room

        <contents of @d>

See the discussion of template expansions at the beginning of this tab
for other possible expansion items.

etmdir

    etmdir: ~/.etm

Absolute path to the directory for etm.cfg and other etm configuration
files.

encoding

    encoding: {file: utf-8, gui: utf-8, term: utf-8}

The encodings to be used for file IO, the GUI and terminal IO.

filechange_alert

    filechange_alert: '/usr/bin/play /home/dag/.etm/sounds/etm_alert.wav'

The command to be executed when etm detects an external change in any of
its data files. Leave this command empty to disable the notification.

fontsize

    fontsize: 13

Use this font size in the gui treeviews.

Mercurial commands

If Mercurial is installed on your system, then the default versions of
the hg commands given below should work without modification. If you
want to use another version control system, then enter the commands for
your version control system. {repo} will be replaced with the internally
generated name of the repository in hg_commit and hg_history, {file}
with the internally generated file name in hg_history, {mesg} with the
internally generated commit message in hg_commit and {0} with the name
of the repository in hg_init.

hg_commit

The command to commit changes to the repository.

    hg_commit: /usr/local/bin/hg commit -A -R {repo} -m '{mesg}'

hg_history

The command to show the history of changes for a particular data file.

    hg_history: '/usr/local/bin/hg log --style compact \
        --template `{rev}: {desc}\n` \
        -R {repo} -p -r `tip`:0 {file}'

hg_init

The command to initialize or create a repository.

    hg_init: /usr/local/bin/hg init {0}

iCalendar files

icscal_file

Pressing F8 in the gui main window will export the selected calendars in
iCalendar format to this file.

    icscal_file: ~/.etm/etmcal.ics

icsitem_file

Pressing F8 in the gui detail view will export the selected item in
iCalendar format to this file.

    icsitem_file: ~/.etm/etmitem.ics

local_timezone

    local_timezone: US/Eastern

This timezone will be used as the default when a value for @z is not
given in an item.

monthly

    monthly: monthly

Relative path from datadir. With the settings above and for datadir the
suggested location for saving new items in, say, October 2012, would be
the file:

    ~/.etm/data/monthly/2012/10.txt

The directories monthly and 2012 and the file 10.txt would, if
necessary, be created. The user could either accept this default or
choose a different file.

report

    report_begin:           '1'
    report_end:             '+1/1'
    report_colors:          2
    report_specifications:  ~/.etm/reports.cfg
    report_width:           54

Report begin and end are fuzzy parsed dates specifying the default
period for reports that group by dates. Each line in the file specified
by report_specifications provides a possible specification for a report.
E.g.

    a MMM yyyy; k[0]; k[1:] -b -1/1 -e 1
    a k, MMM yyyy -b -1/1 -e 1
    c ddd MMM d yyyy
    c f

In the reports dialog these appear in the report specifications pop-up
list. A specification from the list can be selected and, perhaps,
modified or an entirely new specification can be entered. See the
Reports tab for details. See also the agenda settings above.

rowsize

    rowsize: 18

If positive, use this vertical size in GUI tree views.

show_finished

    show_finished: 1

Show this many of the most recent completions of repeated tasks or, if
0, show all completions.

smtp

    smtp_from: dnlgrhm@gmail.com
    smtp_id: dnlgrhm
    smtp_pw: **********
    smtp_server: smtp.gmail.com

Required settings for the smtp server to be used for email alerts.

sms

    sms_message: '!summary!'
    sms_subject: '!time_span!'
    sms_from: dnlgrhm@gmail.com
    sms_pw:  **********
    sms_phone: 0123456789@vtext.com
    sms_server: smtp.gmail.com:587

Required settings for text messaging in alerts. Enter the 10-digit area
code and number and mms extension for the mobile phone to receive the
text message when no numbers are specified in the alert. The illustrated
phone number is for Verizon. Here are the mms extensions for the major
carriers:

    Alltel          @message.alltel.com
    AT&T            @txt.att.net
    Nextel          @messaging.nextel.com
    Sprint          @messaging.sprintpcs.com
    SunCom          @tms.suncom.com
    T-mobile        @tmomail.net
    VoiceStream     @voicestream.net
    Verizon         @vtext.com

sundayfirst

    sundayfirst: false

The setting affects only the twelve month calendar display. The first
column in each month is Sunday if true and Monday otherwise. Both the
week and month views list Monday first regardless of this setting since
both reflect the iso standard for week numbering in which weeks begin
with Monday.

sunmoon_location

    sunmoon_location: [Chapel Hill, NC]

The USNO location for sun/moon data. Either a US city-state 2-tuple such
as [Chapel Hill, NC] or a placename-longitude-latitude 7-tuple such as
[Home, W, 79, 0, N, 35, 54].

Enter a blank value to disable sunmoon information.

weather_location

    weather_location: w=615702

To get the yahoo weather location code (WOEID) go to
http://weather.yahoo.com/, enter your location and hit return. When the
weather page for your location opens, the WOEID will be in the url for
your location, e.g., for Paris, FR the url is

    http://weather.yahoo.com/france/ile-de-france/paris-615702/

and the WOEID is 615702. For US locations you can us the US 5-digit zip
code for your location. E.g. my zip code in Chapel Hill, NC is 27517 and
I would enter

    weather_location: p=27517

Note that p= replaces w= when using a zip code instead of a WOEID. By
default temperatures are given in degrees Farenheit. If you would prefer
Celcius append &u=c to either the WOEID or the zip code in your
weather_location. Note that choosing Celsius degree units changes all
the weather units to metric, for example, wind speed will be reported as
kilometers per hour and barometric pressure as millibars.

Enter a blank value to disable weather information.

weeks_after

    weeks_after: 52

In the day view, all non-repeating, dated items are shown. Additionally
all repetitions of repeating items with a finite number of repetitions
are shown. This includes 'list-only' repeating items and items with &u
(until) or &t (total number of repetitions) entries. For repeating items
with an infinite number of repetitions, those repetitions that occur
within the first weeks_after weeks after the current week are displayed
along with the first repetition after this interval. This assures that
for infrequently repeating items such as voting for president, at least
one repetition will be displayed.

window height and width

    window_height: 428
    window_width: 464

The height and width for the GUI main window.

yearfirst

    yearfirst: true

If yearfirst is true, the YY-MM-DD format will have precedence over
MM-DD-YY in an ambiguous date. See also dayfirst."""
