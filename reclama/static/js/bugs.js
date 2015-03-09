$(document).ajaxStart(function () {
    $("#loading").show();
});

function get_bugs(numbers) {
    $.ajax({
        url: "https://bugzilla.mozilla.org/rest/bug",
        data: {
          id: numbers,
          include_fields: "id,assigned_to,product,resolution,summary,last_change_time,status"
        },
        traditional: true,  // pass id=number several times
        dataType: "json",
    }).done(function(data) {
        $.each(data.bugs, function(i, bug) {
            var number = bug.id
            var bug_summary = "#b" + number;
            var bug_assigned = "#a" + number;
            var bug_product = "#p" + number;
            var bug_modified = "#m" + number;

            var summary = bug.summary;
            var assigned = bug.assigned_to_detail.id;
            var product = bug.product;
            var modified = moment(bug.last_change_time).fromNow();
            var status = bug.status;

            $(bug_summary).text(summary);
            $(bug_product).text("[" + product + "]");
            if (assigned !== 1) {
                $(bug_assigned).text("Assigned");
                $(bug_assigned).addClass("assigned");
            } else {
                $(bug_assigned).text("New");
            }
            if (status == "RESOLVED") {
                $(bug_assigned).removeClass("assigned");
                $(bug_assigned).addClass("resolved");
                $(bug_assigned).text("Resolved");
            }
            $(bug_assigned).parents(".ribbon-wrapper").show();
            $(bug_modified).text("Modified: " + modified);
        });
    });
}

$(document).ajaxStop(function () {
    $("#loading").hide();
});
