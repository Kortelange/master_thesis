DesignsFromGroup := function(name)
    # returns a record that containing the size of the group
    # and a record that indexes representation
    # numbers by the dimension of their representations
    local t, reps, chr, i, d, dims, c;
    c    := CharacterTable(name);
    t    := Irr(c);
    reps := rec();
    dims := [];

    for i in [1 .. Length(t)] do
        chr := t[i];
        if Norm(chr * chr) = 2 then
            d := Degree(chr);
            if not d in dims then
                Add(dims, d);
                reps.(d) := [];
            fi;
            Add(reps.(d), i);
        fi;
    od;
    if Length(RecNames(reps)) > 0 then
        return rec(size := Size(c), dim := reps);
    fi;
    return rec();
end;

GroupDesigns := function(names)
    # returns group designs from a list of names
    local designs, name, reps;
    designs := rec();
    for name in names do
        reps := DesignsFromGroup(name);
        if Length(RecNames(reps)) > 0 then
            designs.(name) := reps;
        fi;
    od;
    return designs;
end;

OrderDesignsByDim := function(designs)
    # returns designs as a record indexed by
    # dimensions and then sizes of groups
    local ordered_designs, dims, name, d, group_designs, tmp, str_size;
    ordered_designs := rec();
    dims            := [];
    for name in RecNames(designs) do
        group_designs := designs.(name);
        for d in RecNames(group_designs.dim) do
            if not Int(d) in dims then
                Add(dims, Int(d));
                ordered_designs.(d) := rec();
            fi;

            tmp      := ordered_designs.(d);
            str_size := String(String(group_designs.size));

            if not str_size in RecNames(tmp) then
                tmp.(str_size) := rec();
            fi;

            tmp.(str_size).(name) := designs.(name).dim.(d);
            ordered_designs.(d)   := tmp;
        od;
    od;
    return ordered_designs;
end;

DesignsByDim := function(names)
    # returns designs ordered by dimension given a list of group names
    return OrderDesignsByDim(GroupDesigns(names));
end;

SortRecNames := function(record)
    return SortedList(
        RecNames(record), function(a, b) return Int(a) < Int(b);
        end);
end;

GetLatexTableElements := function(designs)
    local d, d_rec, size, reps, name, nr, table_elements;
    table_elements := [];
    for d in sortRecNames(designs) do
        d_rec := designs.(d);
        size  := sortRecNames(d_rec)[1];
        reps  := d_rec.(size);
        name  := RecNames(reps)[1];
        nr    := reps.(name)[1];
        Append(table_elements, [[Int(d), Int(size), name, nr]]);
    od;
    return table_elements;
end;

# LoadPackage("Browse");