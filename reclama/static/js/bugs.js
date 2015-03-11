$(document).ajaxStart(function () {
    $("#loading").show();
});

function unique(array) {
    return $.grep(array, function(el, index) {
        return index === $.inArray(el, array);
    });
}

function get_bugs(numbers) {
    var items = new Array();

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

            items.push(product);

            $(bug_summary).text(summary);
            $(bug_product).text("[" + product + "]");
            $(bug_product).parents(".bug").addClass(product.replace(/\s/g, ''))
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
            $(bug_modified).text("modified " + modified);
        });
        products = unique(items);
        $.each(products, function(index, product) {
            $('<option>').val(product).text(product).appendTo('#product-selection');
        });
    });

    $('#product-selection').change( function() {
        var product = $(this).val();
        if (product == "0") {
            $(".bug").show();
        } else {
            $(".bug").hide();
            $("." + product.replace(/\s/g, '')).show();
        }
    });
}

$(document).ajaxStop(function () {
    $("#loading").hide();
});
